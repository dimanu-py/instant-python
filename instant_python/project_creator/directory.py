from pathlib import Path

from instant_python.project_creator.node import Node


class Directory:
    def __init__(self, name: str, is_python: bool, children: list[Node]) -> None:
        self._name = name
        self._is_python = is_python
        self._children = children

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, is_python={self._is_python}, children={self._children})"

    def create(self, base_path: Path) -> None:
        path = base_path / self._name
        path.mkdir(parents=True, exist_ok=True)
