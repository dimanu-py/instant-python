import yaml

from instant_python.configuration.configuration_schema import ConfigurationSchema
from instant_python.configuration.parser.configuration_file_not_found import (
    ConfigurationFileNotFound,
)
from instant_python.configuration.parser.empty_configuration_not_allowed import (
    EmptyConfigurationNotAllowed,
)


class Parser:
    @classmethod
    def parse(cls, config_file_path: str) -> ConfigurationSchema:
        content = cls._get_config_file_content(config_file_path)
        return content

    @classmethod
    def _get_config_file_content(cls, config_file_path: str) -> dict[str, dict]:
        content = cls._read_config_file(config_file_path)
        cls._ensure_config_file_is_not_empty(content)
        return content

    @staticmethod
    def _ensure_config_file_is_not_empty(content: dict[str, dict]) -> None:
        if not content:
            raise EmptyConfigurationNotAllowed()

    @staticmethod
    def _read_config_file(config_file_path: str) -> dict[str, dict]:
        try:
            with open(config_file_path, "r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise ConfigurationFileNotFound(config_file_path)
