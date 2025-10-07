from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.configuration_schema import ConfigurationSchema
from instant_python.configuration.parser.empty_configuration_not_allowed import EmptyConfigurationNotAllowed


class Parser(ConfigParser):
    def parse(self, content: dict[str, dict]) -> ConfigurationSchema:
        raise EmptyConfigurationNotAllowed
