from pathlib import Path

from instant_python.project_generator.node import Node


class PythonModule(Node):
    INIT_FILE = "__init__.py"

    def __init__(self, name: str, children: list = None) -> None:
        self._name = name
        self._children = children or []

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self._name}, children={self._children})"
        )

    def create(self, base_path: Path) -> None:
        module_path = base_path/ self._name
        module_path.mkdir(parents=True, exist_ok=True)
        init_path = module_path / self.INIT_FILE
        init_path.touch(exist_ok=True)

        for child in self._children:
            child.create(base_path=module_path)

