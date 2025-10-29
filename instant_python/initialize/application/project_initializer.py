from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_renderer import ProjectRenderer


class ProjectInitializer:
    def __init__(
        self,
        renderer: ProjectRenderer,
    ) -> None:
        self._project_renderer = renderer

    def execute(self, config: ConfigSchema) -> None:
        project_structure = self._project_renderer.render_project_structure(context_config=config)
