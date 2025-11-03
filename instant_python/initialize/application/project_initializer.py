from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.domain.project_writer import ProjectWriter


class ProjectInitializer:
    def __init__(
        self,
        renderer: ProjectRenderer,
        writer: ProjectWriter,
    ) -> None:
        self._project_renderer = renderer
        self._writer = writer

    def execute(self, config: ConfigSchema) -> None:
        _ = self._project_renderer.render(context_config=config)
