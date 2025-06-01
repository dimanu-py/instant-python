from instant_python.configuration.configuration_schema import ConfigurationSchema
from instant_python.configuration.parser.configuration_file_not_found import ConfigurationFileNotFound


class Parser:
    @classmethod
    def parse(cls, config_file_path: str) -> ConfigurationSchema:
        raise ConfigurationFileNotFound(config_file_path)
