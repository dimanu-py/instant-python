import yaml

from instant_python.render.jinja_environment import JinjaEnvironment
from instant_python.configuration.configuration_schema import ConfigurationSchema


class JinjaProjectRenderer:
    _MAIN_STRUCTURE_TEMPLATE = "main_structure.yml.j2"

    def __init__(self, jinja_environment: JinjaEnvironment) -> None:
        self._jinja_environment = jinja_environment

    def render_project_structure(self, context_config: ConfigurationSchema, template_base_dir: str) -> list[dict]:
        """Render the project structure based on the provided configuration.

        Args:
            context_config: The configuration schema containing the context for rendering.
            template_base_dir: The base directory where the templates are located.

        Returns:
            The structure of files and directories for the project as a dictionary.
        """
        template_name = self._get_main_structure_template_path(context_config, template_base_dir)
        raw_project_structure = self._jinja_environment.render_template(
            name=template_name, context=context_config.to_primitives()
        )
        return yaml.safe_load(raw_project_structure)

    def _get_main_structure_template_path(self, context_config: ConfigurationSchema, template_base_dir: str) -> str:
        return f"{template_base_dir}/{context_config.template_type}/{self._MAIN_STRUCTURE_TEMPLATE}"
