from pathlib import Path

from instant_python.project_generator.node import Node


class Directory(Node):
	_INIT_FILE = "__init__.py"

	def __init__(self, name: str, children: list[Node], python_module: bool) -> None:
		self._name = name
		self._python_module = python_module
		self._children = children

	def __repr__(self) -> str:
		return (
			f"{self.__class__.__name__}(name={self._name}, children={self._children})"
		)

	def create(self, base_path: Path) -> None:
		directory_path = base_path / self._name
		directory_path.mkdir(parents=True, exist_ok=True)

		if self._python_module:
			init_path = directory_path / self._INIT_FILE
			init_path.touch(exist_ok=True)

		for child in self._children:
			child.create(base_path=directory_path)