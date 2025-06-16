from pathlib import Path

from instant_python.configuration.configuration_schema import ConfigurationSchema
from instant_python.project_creator.node import Node
from instant_python.render.jinja_environment import JinjaEnvironment


class File(Node):
    def __init__(self, name: str, extension: str) -> None:
        self._file_name = f"{name.split('/')[-1]}{extension}"
        self._file_path = None
        self._template_path = f"boilerplate/{name}{extension}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._file_name})"

    def create(self, base_path: Path) -> None:
        self._file_path = base_path / self._file_name
        self._file_path.touch(exist_ok=True)

    def fill(self, renderer: JinjaEnvironment, context_config: ConfigurationSchema) -> None:
        content = renderer.render_template(
            name=self._template_path,
            context=context_config.to_primitives(),
        )
        self._file_path.write_text(content)
