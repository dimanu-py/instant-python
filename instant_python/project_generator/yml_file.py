from pathlib import Path

from instant_python.project_generator.node import Node
from instant_python.project_generator.template_manager import TemplateManager


class YmlFile(Node):
	_EXTENSION = ".yml"

	def __init__(self, name: str) -> None:
		self._name = name
		self._template_manager = TemplateManager()

	def __repr__(self) -> str:
		return f"{self.__class__.__name__}(name={self._name}, content={self._content})"

	def create(self, base_path: Path) -> None:
		file_name = f"{self._name}{self._EXTENSION}"
		file_path = base_path / file_name

		template_path = Path("boilerplate") / file_name
		content = self._template_manager.get_boilerplate(str(template_path))
		file_path.write_text(content)
