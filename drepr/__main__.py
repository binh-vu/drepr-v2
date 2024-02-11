from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Annotated, Optional

import typer

from drepr.models.prelude import DRepr
from drepr.planning.class_map_plan import ClassesMapExecutionPlan
from drepr.program_generation.main import gen_program


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
):
    parsed_resources = [ResourceInput.from_string(r) for r in resource]
    parsed_repr = DRepr.parse_from_file(repr)
    exec_plan = ClassesMapExecutionPlan.create(parsed_repr)

    prog = gen_program(parsed_repr, exec_plan).to_python()
    if progfile is not None:
        with open(progfile, "w") as f:
            f.write(prog)


if __name__ == "__main__":
    typer.run(main)
