import yaml

from instant_python.builder.jinja_environment import JinjaEnvironment
from instant_python.configuration.configuration_schema import ConfigurationSchema


class JinjaProjectRender:
    def __init__(self, jinja_environment: JinjaEnvironment) -> None:
        self._jinja_environment = jinja_environment

    def get_project(self, context_config: ConfigurationSchema) -> dict[str, list[dict]]:
        template_type = context_config.template.name
        template_name = f"project_structure/{template_type}/main_structure.yml.j2"
        raw_project_structure = self._jinja_environment.render_template(name=template_name, context=context_config.to_primitives())
        return yaml.safe_load(raw_project_structure)
