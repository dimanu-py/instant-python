from typing import Union

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
    def parse_from_file(cls, config_file_path: str) -> ConfigurationSchema:
        """Parses the configuration file and validates its content.

        Args:
            config_file_path: The path to the configuration file to be parsed.
        Returns:
            ConfigurationSchema: An instance of ConfigurationSchema containing the parsed configuration.
        Raises:
            ConfigurationFileNotFound: If the configuration file does not exist in that path.
            EmptyConfigurationNotAllowed: If the configuration file is empty.
            ConfigKeyNotPresent: If any of the required keys are missing from the configuration.
            MissingMandatoryFields: If any mandatory fields are missing in the configuration sections.
        """
        content = cls._get_config_file_content(config_file_path)
        general_configuration, dependencies_configuration, template_configuration, git_configuration = (
            cls._parse_configuration(content=content)
        )
        return ConfigurationSchema.from_file(
            config_file_path=config_file_path,
            general=general_configuration,
            dependencies=dependencies_configuration,
            template=template_configuration,
            git=git_configuration,
        )

    @classmethod
    def parse_from_answers(cls, content: dict[str, dict]) -> ConfigurationSchema:
        general_configuration, dependencies_configuration, template_configuration, git_configuration = (
            cls._parse_configuration(content=content)
        )
        return ConfigurationSchema(
            general=general_configuration,
            dependencies=dependencies_configuration,
            template=template_configuration,
            git=git_configuration,
        )

    @classmethod
    def _parse_configuration(cls, content: dict[str, dict]) -> tuple:
        general_configuration = cls._parse_general_configuration(content["general"])
        dependencies_configuration = cls._parse_dependencies_configuration(content["dependencies"])
        template_configuration = cls._parse_template_configuration(content["template"])
        git_configuration = cls._parse_git_configuration(content["git"])
        return general_configuration, dependencies_configuration, template_configuration, git_configuration

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
            _ensure_error_is_for_missing_fields(error)
            raise MissingMandatoryFields(error.args[0], "general") from error

    @staticmethod
    def _parse_dependencies_configuration(
        fields: list[dict[str, Union[str, bool]]],
    ) -> list[DependencyConfiguration]:
        dependencies = []

        if not fields:
            return dependencies

        for dependency_fields in fields:
            try:
                dependency = DependencyConfiguration(**dependency_fields)
            except TypeError as error:
                _ensure_error_is_for_missing_fields(error)
                raise MissingMandatoryFields(error.args[0], "dependencies") from error

            dependencies.append(dependency)

        return dependencies

    @staticmethod
    def _parse_template_configuration(fields: dict[str, Union[str, bool, list[str]]]) -> TemplateConfiguration:
        try:
            return TemplateConfiguration(**fields)
        except TypeError as error:
            _ensure_error_is_for_missing_fields(error)
            raise MissingMandatoryFields(error.args[0], "template") from error

    @staticmethod
    def _parse_git_configuration(fields: dict[str, Union[str, bool]]) -> GitConfiguration:
        try:
            return GitConfiguration(**fields)
        except TypeError as error:
            _ensure_error_is_for_missing_fields(error)
            raise MissingMandatoryFields(error.args[0], "git") from error


def _ensure_error_is_for_missing_fields(error: TypeError) -> None:
    if ".__init__() missing" not in str(error):
        raise error
