from instant_python.config.domain.configuration_schema import ConfigurationSchema
from instant_python.initialize.domain.project_renderer import ProjectRenderer


class ProjectInitializer:
    def __init__(
        self,
        renderer: ProjectRenderer,
    ) -> None:
        self._project_renderer = renderer

    def execute(self, config: ConfigurationSchema) -> None: ...
