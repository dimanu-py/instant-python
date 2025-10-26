from typing import Union

from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.config.domain.dependency_config import DependencyConfig
from instant_python.config.domain.general_config import GeneralConfig
from instant_python.config.domain.git_config import GitConfig
from instant_python.config.domain.template_config import TemplateConfig
from instant_python.config.infra.parser.errors import (
    ConfigKeyNotPresent,
    EmptyConfigurationNotAllowed,
    MissingMandatoryFields,
)


class Parser(ConfigParser):
    _GENERAL = "general"
    _DEPENDENCIES = "dependencies"
    _TEMPLATE = "template"
    _GIT = "git"
    _REQUIRED_CONFIG_KEYS = [_GENERAL, _DEPENDENCIES, _TEMPLATE, _GIT]

    def parse(self, content: dict[str, dict], custom_config_path: Union[str, None] = None) -> ConfigSchema:
        self._ensure_config_is_not_empty(content)
        self._ensure_all_required_sections_are_present(content)
        general_section = self._parse_general_section(content[self._GENERAL])
        dependencies_section = self._parse_dependencies_section(content[self._DEPENDENCIES])
        template_section = self._parse_template_section(content[self._TEMPLATE])
        git_section = self._parse_git_section(content[self._GIT])
        return (
            ConfigSchema(
                general=general_section,
                dependencies=dependencies_section,
                template=template_section,
                git=git_section,
            )
            if not custom_config_path
            else ConfigSchema.from_file(
                config_file_path=custom_config_path,
                general=general_section,
                dependencies=dependencies_section,
                template=template_section,
                git=git_section,
            )
        )

    def _parse_general_section(self, fields: dict[str, str]) -> GeneralConfig:
        try:
            return GeneralConfig(**fields)
        except TypeError as error:
            self._ensure_error_is_for_missing_fields(error)
            raise MissingMandatoryFields(error.args[0], self._GENERAL) from error

    def _parse_dependencies_section(
        self,
        fields: list[dict[str, Union[str, bool]]],
    ) -> list[DependencyConfig]:
        dependencies = []

        if not fields:
            return dependencies

        for dependency_fields in fields:
            try:
                dependency = DependencyConfig(**dependency_fields)
            except TypeError as error:
                self._ensure_error_is_for_missing_fields(error)
                raise MissingMandatoryFields(error.args[0], self._DEPENDENCIES) from error

            dependencies.append(dependency)

        return dependencies

    def _parse_template_section(self, fields: dict[str, Union[str, bool, list[str]]]) -> TemplateConfig:
        try:
            return TemplateConfig(**fields)
        except TypeError as error:
            self._ensure_error_is_for_missing_fields(error)
            raise MissingMandatoryFields(error.args[0], self._TEMPLATE) from error

    def _parse_git_section(self, fields: dict[str, Union[str, bool]]) -> GitConfig:
        try:
            return GitConfig(**fields)
        except TypeError as error:
            self._ensure_error_is_for_missing_fields(error)
            raise MissingMandatoryFields(error.args[0], self._GIT) from error

    def _ensure_all_required_sections_are_present(self, content: dict[str, dict]):
        missing_keys = [key for key in self._REQUIRED_CONFIG_KEYS if key not in content]
        if missing_keys:
            raise ConfigKeyNotPresent(missing_keys, self._REQUIRED_CONFIG_KEYS)

    @staticmethod
    def _ensure_config_is_not_empty(content: dict[str, dict]):
        if not content:
            raise EmptyConfigurationNotAllowed

    @staticmethod
    def _ensure_error_is_for_missing_fields(error: TypeError) -> None:
        if ".__init__() missing" not in str(error):
            raise error
