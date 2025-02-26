from pathlib import Path

from instant_python.project_generator.node import Node


class Directory(Node):
	def __init__(self, name: str, children: list = None) -> None:
		self._name = name
		self._children = children or []

	def __repr__(self) -> str:
		return (
			f"{self.__class__.__name__}(name={self._name}, children={self._children})"
		)

	def create(self, base_path: Path) -> None:
		directory_path = base_path / self._name
		directory_path.mkdir(parents=True, exist_ok=True)

		for child in self._children:
			child.create(base_path=directory_path)