from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment


class JinjaProjectRenderer(ProjectRenderer):
    def __init__(self, env: JinjaEnvironment) -> None:
        self._env = env

    def render_project_structure(self, context_config: ConfigSchema) -> list[dict]:
        raise NotImplementedError
