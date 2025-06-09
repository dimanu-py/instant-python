from pathlib import Path

from instant_python.project_creator.node import Node


class BoilerplateFile(Node):
    def __init__(self, name: str, extension: str) -> None:
        self._file_name = f"{name.split('/')[-1]}{extension}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._file_name})"

    def create(self, base_path: Path) -> None:
        raise NotImplementedError
