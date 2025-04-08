from pathlib import Path

from instant_python.project_generator.default_template_manager import DefaultTemplateManager
from instant_python.project_generator.node import Node


class File(Node):

    def __init__(self, name: str, extension: str) -> None:
        self._file_name = f"{name.split('/')[-1]}{extension}"
        self._template_path = f"boilerplate/{name}{extension}"
        self._template_manager = DefaultTemplateManager()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._file_name})"

    def create(self, base_path: Path) -> None:
        file_path = base_path / self._file_name
        content = self._template_manager.get_boilerplate(self._template_path)
        file_path.write_text(content)
