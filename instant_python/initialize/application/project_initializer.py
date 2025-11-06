from pathlib import Path

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.env_manager import EnvManager
from instant_python.initialize.domain.project_formatter import ProjectFormatter
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.domain.project_writer import ProjectWriter
from instant_python.initialize.domain.version_control_configurer import VersionControlConfigurer


class ProjectInitializer:
    def __init__(
        self,
        renderer: ProjectRenderer,
        writer: ProjectWriter,
        env_manager: EnvManager,
        version_control_configurer: VersionControlConfigurer,
        formatter: ProjectFormatter,
    ) -> None:
        self._project_renderer = renderer
        self._writer = writer
        self._env_manager = env_manager
        self._version_control_configurer = version_control_configurer
        self._formatter = formatter

    def execute(self, config: ConfigSchema, destination_project_folder: Path) -> None:
        project_structure = self._project_renderer.render(context_config=config)
        self._writer.write(project_structure=project_structure, destination=destination_project_folder)
        self._env_manager.setup(
            python_version=config.python_version,
            dependencies=config.dependencies,
        )
        if config.version_control_has_to_be_initialized:
            self._version_control_configurer.setup(config.git)
        self._formatter.format()
