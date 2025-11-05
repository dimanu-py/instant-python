from pathlib import Path

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.formatter.project_formatter import ProjectFormatter
from instant_python.initialize.domain.env_manager import EnvManager
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.domain.project_writer import ProjectWriter


class ProjectInitializer:
    def __init__(
        self,
        renderer: ProjectRenderer,
        writer: ProjectWriter,
        env_manager: EnvManager,
        formatter: ProjectFormatter,
    ) -> None:
        self._project_renderer = renderer
        self._writer = writer
        self._env_manager = env_manager
        self._formatter = formatter

    def execute(self, config: ConfigSchema, destination_project_folder: Path) -> None:
        project_structure = self._project_renderer.render(context_config=config)
        self._writer.write(project_structure=project_structure, destination=destination_project_folder)
        self._env_manager.setup(
            python_version=config.python_version,
            dependencies=config.dependencies,
        )
        self._formatter.format()
