from pathlib import Path

from instant_python.project_generator.node import Node


class PythonFile(Node):
    def __init__(self, name: str) -> None:
        self._name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name})"

    def create(self, base_path: Path) -> None:
        raise NotImplementedError
