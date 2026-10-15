import tomllib
from pathlib import Path


def test_project_declares_supported_python_version() -> None:
    project_file = Path(__file__).parents[2] / "pyproject.toml"
    with project_file.open("rb") as file:
        project = tomllib.load(file)

    assert project["project"]["requires-python"] == ">=3.12,<3.13"
