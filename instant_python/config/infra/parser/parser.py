from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.configuration_schema import ConfigurationSchema


class Parser(ConfigParser):
    def parse(self, content: dict[str, dict]) -> ConfigurationSchema:
        raise NotImplementedError
