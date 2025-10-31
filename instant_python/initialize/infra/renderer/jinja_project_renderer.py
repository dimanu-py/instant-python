import yaml

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment


class JinjaProjectRenderer(ProjectRenderer):
    _MAIN_STRUCTURE_TEMPLATE_FILE = "main_structure.yml.j2"

    def __init__(self, env: JinjaEnvironment) -> None:
        self._env = env

    def render(self, context_config: ConfigSchema) -> list[dict]:
        template_name = self._get_project_main_structure_template(context_config.template_type)
        return self._render_project_structure_with_jinja(context_config, template_name)

    def _render_project_structure_with_jinja(self, context_config: ConfigSchema, template_name: str) -> list[dict]:
        raw_project_structure = self._env.render_template(
            name=template_name, context=context_config.to_primitives()
        )
        return yaml.safe_load(raw_project_structure)

    def _get_project_main_structure_template(self, template_type: str) -> str:
        return f"{template_type}/{self._MAIN_STRUCTURE_TEMPLATE_FILE}"
