from instant_python.builder.jinja_environment import JinjaEnvironment
from instant_python.configuration.configuration_schema import ConfigurationSchema


class JinjaProjectRender:
    def __init__(self, jinja_environment: JinjaEnvironment) -> None:
        self._jinja_environment = jinja_environment

    def get_project(self, context_config: ConfigurationSchema) -> dict[str, list[dict]]:
        raise NotImplementedError()
