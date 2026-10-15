import tomllib
from pathlib import Path


def _requires_python() -> str:
    project_file = Path(__file__).parents[2] / "pyproject.toml"
    with project_file.open("rb") as file:
        return tomllib.load(file)["project"]["requires-python"]


def test_project_declares_supported_python_version() -> None:
    assert _requires_python().startswith(">=3.12")


def test_python_version_files_agree() -> None:
    version_file = Path(__file__).parents[2] / ".python-version"
    version = version_file.read_text(encoding="utf-8").strip()
    assert _requires_python().startswith(f">={version}")
