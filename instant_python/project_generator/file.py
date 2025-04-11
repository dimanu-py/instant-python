from pathlib import Path

from instant_python.project_generator.node import Node


class File(Node):
    def __init__(self, name: str, extension: str) -> None:
        self._file_name = name
        self._extension = extension

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._file_name})"

    def create(self, base_path: Path) -> None:
        file_path = base_path / f"{self._file_name}{self._extension}"
        file_path.touch(exist_ok=True)
