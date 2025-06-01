import yaml

from instant_python.configuration.config_key_not_present import ConfigKeyNotPresent
from instant_python.configuration.configuration_schema import ConfigurationSchema
from instant_python.configuration.general.general_configuration import (
    GeneralConfiguration,
)
from instant_python.configuration.parser.configuration_file_not_found import (
    ConfigurationFileNotFound,
)
from instant_python.configuration.parser.empty_configuration_not_allowed import (
    EmptyConfigurationNotAllowed,
)
from instant_python.configuration.parser.missing_mandatory_fields import MissingMandatoryFields


class Parser:
    REQUIRED_CONFIG_KEYS = ["general", "dependencies", "template", "git"]

    @classmethod
    def parse(cls, config_file_path: str) -> ConfigurationSchema:
        content = cls._get_config_file_content(config_file_path)

        general_configuration = cls._parse_general_configuration(content["general"])
        return ConfigurationSchema(
            general=general_configuration,
        )

    @classmethod
    def _get_config_file_content(cls, config_file_path: str) -> dict[str, dict]:
        content = cls._read_config_file(config_file_path)
        cls._ensure_config_file_is_not_empty(content)
        cls._ensure_all_required_keys_are_present(content)
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

    @staticmethod
    def _ensure_all_required_keys_are_present(content: dict[str, dict]) -> None:
        missing_keys = [
            key for key in Parser.REQUIRED_CONFIG_KEYS if key not in content
        ]
        if missing_keys:
            raise ConfigKeyNotPresent(missing_keys, Parser.REQUIRED_CONFIG_KEYS)

    @staticmethod
    def _parse_general_configuration(fields: dict[str, str]) -> GeneralConfiguration:
        try:
            return GeneralConfiguration(
                slug=fields["slug"],
                source_name=fields["source_name"],
                description=fields["description"],
                version=str(fields["version"]),
                author=fields["author"],
                license=fields["license"],
                python_version=str(fields["python_version"]),
                dependency_manager=fields["dependency_manager"],
            )
        except KeyError as error:
            raise MissingMandatoryFields(error.args[0], "general") from error

