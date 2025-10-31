import yaml

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment


class JinjaProjectRenderer(ProjectRenderer):
    _MAIN_STRUCTURE_TEMPLATE_FILE = "main_structure.yml.j2"

    def __init__(self, env: JinjaEnvironment) -> None:
        self._env = env

    def render(self, context_config: ConfigSchema) -> list[dict]:
        template_name = f"{context_config.template_type}/{self._MAIN_STRUCTURE_TEMPLATE_FILE}"
        raw_project_structure = self._env.render_template(
            name=template_name, context=context_config.to_primitives()
        )
        return yaml.safe_load(raw_project_structure)