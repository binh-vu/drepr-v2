from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Optional
from uuid import uuid4

from drepr.models.prelude import DRepr, OutputFormat
from drepr.planning.class_map_plan import ClassesMapExecutionPlan
from drepr.program_generation.main import FileOutput, MemoryOutput, gen_program


def convert(
    repr: DRepr | Path,
    resources: dict[str, Path],
    progfile: Optional[Path] = None,
    outfile: Optional[Path] = None,
    format: OutputFormat = OutputFormat.TTL,
    tmpdir: Path = Path("/tmp/drepr"),
    debuginfo: bool = False,
    cleanup: bool = True,
):
    if not isinstance(repr, DRepr):
        repr = DRepr.parse_from_file(repr)

    exec_plan = ClassesMapExecutionPlan.create(repr)

    if outfile is not None:
        output = FileOutput(outfile, format)
    else:
        output = MemoryOutput(format)

    prog = gen_program(exec_plan.desc, exec_plan, output, debuginfo).to_python()
    cleanup = progfile is None
    if progfile is not None:
        with open(progfile, "w") as f:
            f.write(prog)
    else:
        tmpdir.mkdir(parents=True, exist_ok=True)
        unique_id = str(uuid4()).replace("-", "_")
        progfile = tmpdir / f"main_{unique_id}.py"
        progfile.write_text(prog)

    spec = importlib.util.spec_from_file_location("drepr_prog", progfile)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if outfile is not None:
        output = module.main(
            *[
                resources[r.id]
                for r in exec_plan.desc.resources
                if not r.is_preprocessing_output()
            ],
            outfile,
        )
    else:
        output = module.main(
            *[
                resources[r.id]
                for r in exec_plan.desc.resources
                if not r.is_preprocessing_output()
            ]
        )

    if cleanup:
        progfile.unlink()

    return output