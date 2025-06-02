import yaml

from instant_python.configuration.parser.config_key_not_present import ConfigKeyNotPresent
from instant_python.configuration.configuration_schema import ConfigurationSchema
from instant_python.configuration.dependency.dependency_configuration import (
    DependencyConfiguration,
)
from instant_python.configuration.general.general_configuration import (
    GeneralConfiguration,
)
from instant_python.configuration.git.git_configuration import GitConfiguration
from instant_python.configuration.parser.configuration_file_not_found import (
    ConfigurationFileNotFound,
)
from instant_python.configuration.parser.empty_configuration_not_allowed import (
    EmptyConfigurationNotAllowed,
)
from instant_python.configuration.parser.missing_mandatory_fields import (
    MissingMandatoryFields,
)
from instant_python.configuration.template.template_configuration import TemplateConfiguration


class Parser:
    REQUIRED_CONFIG_KEYS = ["general", "dependencies", "template", "git"]

    @classmethod
    def parse(cls, config_file_path: str) -> ConfigurationSchema:
        content = cls._get_config_file_content(config_file_path)

        general_configuration = cls._parse_general_configuration(content["general"])
        dependencies_configuration = cls._parse_dependencies_configuration(content["dependencies"])
        template_configuration = cls._parse_template_configuration(content["template"])
        git_configuration = cls._parse_git_configuration(content["git"])

        return ConfigurationSchema(
            general=general_configuration,
            dependencies=dependencies_configuration,
            template=template_configuration,
            git=git_configuration,
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
        missing_keys = [key for key in Parser.REQUIRED_CONFIG_KEYS if key not in content]
        if missing_keys:
            raise ConfigKeyNotPresent(missing_keys, Parser.REQUIRED_CONFIG_KEYS)

    @staticmethod
    def _parse_general_configuration(fields: dict[str, str]) -> GeneralConfiguration:
        try:
            return GeneralConfiguration(**fields)
        except TypeError as error:
            raise MissingMandatoryFields(error.args[0], "general") from error

    @staticmethod
    def _parse_dependencies_configuration(
        fields: list[dict[str, str | bool]],
    ) -> list[DependencyConfiguration]:
        dependencies = []
        for dependency_fields in fields:
            try:
                dependency = DependencyConfiguration(**dependency_fields)
            except TypeError as error:
                raise MissingMandatoryFields(error.args[0], "dependencies") from error

            dependencies.append(dependency)

        return dependencies

    @staticmethod
    def _parse_template_configuration(fields: dict[str, str | bool | list[str]]) -> TemplateConfiguration:
        try:
            return TemplateConfiguration(**fields)
        except TypeError as error:
            raise MissingMandatoryFields(error.args[0], "template") from error

    @staticmethod
    def _parse_git_configuration(fields: dict[str, str | bool]) -> GitConfiguration:
        try:
            return GitConfiguration(**fields)
        except TypeError as error:
            raise MissingMandatoryFields(error.args[0], "git") from error
