import yaml

from instant_python.configuration.configuration_schema import ConfigurationSchema
from instant_python.configuration.parser.configuration_file_not_found import (
    ConfigurationFileNotFound,
)
from instant_python.configuration.parser.empty_configuration_not_allowed import EmptyConfigurationNotAllowed


class Parser:
    @classmethod
    def parse(cls, config_file_path: str) -> ConfigurationSchema:
        try:
            with open(config_file_path, "r") as file:
                content = yaml.safe_load(file)
        except FileNotFoundError:
            raise ConfigurationFileNotFound(config_file_path)

        if not content:
            raise EmptyConfigurationNotAllowed()

        return content