from pathlib import Path

from instant_python.project_creator.node import Node


class Directory(Node):
    _INIT_FILE = "__init__.py"

    def __init__(self, name: str, is_python: bool, children: list[Node]) -> None:
        self._name = name
        self._is_python_module = is_python
        self._children = children

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, is_python={self._is_python_module}, children={self._children})"

    def create(self, base_path: Path) -> None:
        path = base_path / self._name
        path.mkdir(parents=True, exist_ok=True)

        if self._is_python_module:
            init_file_path = path / self._INIT_FILE
            init_file_path.touch(exist_ok=True)

        for child in self._children:
            child.create(base_path=path)
