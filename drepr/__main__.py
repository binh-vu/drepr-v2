from __future__ import annotations

import importlib.util
from dataclasses import dataclass
from pathlib import Path
from threading import local
from typing import Annotated, Optional

import typer

from drepr.models.prelude import DRepr, OutputFormat
from drepr.planning.class_map_plan import ClassesMapExecutionPlan
from drepr.program_generation.main import FileOutput, MemoryOutput, Output, gen_program

app = typer.Typer(pretty_exceptions_short=True, pretty_exceptions_enable=False)


@dataclass
class ResourceInput:
    id: str
    file: Path

    @staticmethod
    def from_string(value: str) -> ResourceInput:
        lst = value.split("=", 1)
        if len(lst) != 2:
            raise Exception(f"Invalid resource format. Expect <id>`=`<file_path>")

        id, file = lst
        file = Path(file)
        if not file.exists():
            raise Exception(f"Resource file `{file}` does not exist")

        return ResourceInput(id, file)


@app.command()
def main(
    repr: Annotated[
        Path,
        typer.Option(
            help="A path to a file containing representation (support 2 formats: JSON & YML)",
            exists=True,
            dir_okay=False,
        ),
    ],
    resource: Annotated[
        list[str],
        typer.Option(
            help="file paths of resources in this format: <resource_id>=<file_path>",
        ),
    ],
    progfile: Annotated[
        Optional[Path],
        typer.Option(
            help="A path to a file to save the generated program", exists=False
        ),
    ] = None,
    outfile: Annotated[
        Optional[Path],
        typer.Option(
            help="A path to a file to save the transformed data", exists=False
        ),
    ] = None,
    format: Annotated[
        OutputFormat,
        typer.Option(
            help="The output format",
        ),
    ] = OutputFormat.TTL,
    tmpdir: Annotated[
        Path,
        typer.Option(
            help="A directory to save temporary files",
            default=Path("/tmp/drepr"),
        ),
    ] = Path("/tmp/drepr"),
):
    parsed_resources = {
        (x := ResourceInput.from_string(r)).id: x.file for r in resource
    }
    parsed_repr = DRepr.parse_from_file(repr)
    exec_plan = ClassesMapExecutionPlan.create(parsed_repr)

    if outfile is not None:
        output = FileOutput(outfile, format)
    else:
        output = MemoryOutput(format)

    prog = gen_program(parsed_repr, exec_plan, output).to_python()
    if progfile is not None:
        with open(progfile, "w") as f:
            f.write(prog)

    tmpdir.mkdir(parents=True, exist_ok=True)
    (tmpdir / "main.py").write_text(prog)

    spec = importlib.util.spec_from_file_location("drepr_prog", tmpdir / "main.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if outfile is not None:
        module.main(*[parsed_resources[r.id] for r in parsed_repr.resources], outfile)
    else:
        print(module.main(*[parsed_resources[r.id] for r in parsed_repr.resources]))


if __name__ == "__main__":
    app()
