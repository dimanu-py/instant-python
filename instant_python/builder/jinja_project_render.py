import yaml

from instant_python.builder.jinja_environment import JinjaEnvironment
from instant_python.configuration.configuration_schema import ConfigurationSchema


class JinjaProjectRender:
    _DEFAULT_TEMPLATE_BASE_DIR = "project_structure"
    _DEFAULT_MAIN_STRUCTURE_TEMPLATE = "main_structure.yml.j2"

    def __init__(
        self,
        jinja_environment: JinjaEnvironment,
        template_base_dir: str | None = None,
        main_structure_template: str | None = None
    ) -> None:
        self._jinja_environment = jinja_environment
        self._template_base_dir = template_base_dir or self._DEFAULT_TEMPLATE_BASE_DIR
        self._main_structure_template = main_structure_template or self._DEFAULT_MAIN_STRUCTURE_TEMPLATE

    def render_project_structure(self, context_config: ConfigurationSchema) -> dict[str, list[dict]]:
        template_name = self._get_main_structure_template_path(context_config)
        raw_project_structure = self._jinja_environment.render_template(name=template_name, context=context_config.to_primitives())
        return yaml.safe_load(raw_project_structure)

    def _get_main_structure_template_path(self, context_config: ConfigurationSchema) -> str:
        return f"{self._template_base_dir}/{context_config.template_type}/{self._main_structure_template}"
