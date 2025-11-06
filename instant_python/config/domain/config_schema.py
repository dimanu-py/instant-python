import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import TypedDict, Union

from instant_python.config.domain.dependency_config import (
    DependencyConfig,
)
from instant_python.config.domain.general_config import (
    GeneralConfig,
)
from instant_python.config.domain.git_config import GitConfig
from instant_python.config.domain.template_config import (
    TemplateConfig,
)
from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes

_GENERAL = "general"
_DEPENDENCIES = "dependencies"
_TEMPLATE = "template"
_GIT = "git"
_REQUIRED_CONFIG_KEYS = [_GENERAL, _DEPENDENCIES, _TEMPLATE, _GIT]


@dataclass
class ConfigSchema:
    general: GeneralConfig
    dependencies: list[DependencyConfig]
    template: TemplateConfig
    git: GitConfig
    config_file_path: Path = field(default_factory=lambda: ConfigSchema._DEFAULT_CONFIG_PATH)

    _DEFAULT_CONFIG_PATH: Path = Path("ipy.yml")

    @classmethod
    def from_primitives(
        cls, content: dict[str, Union[dict, list]], custom_config_path: Union[str, None] = None
    ) -> "ConfigSchema":
        cls._ensure_config_is_not_empty(content)
        cls._ensure_all_required_sections_are_present(content)
        return cls(
            general=GeneralConfig(**content[_GENERAL]),
            dependencies=[DependencyConfig(**dep) for dep in content[_DEPENDENCIES]] if content[_DEPENDENCIES] else [],
            template=TemplateConfig(**content[_TEMPLATE]),
            git=GitConfig(**content[_GIT]),
            config_file_path=Path(custom_config_path) if custom_config_path else cls._DEFAULT_CONFIG_PATH,
        )

    @classmethod
    def _ensure_config_is_not_empty(cls, content: dict[str, Union[dict, list]]) -> None:
        if not content:
            raise EmptyConfigurationNotAllowed

    @classmethod
    def _ensure_all_required_sections_are_present(cls, content: dict[str, Union[dict, list]]):
        missing_keys = [key for key in _REQUIRED_CONFIG_KEYS if key not in content]
        if missing_keys:
            raise ConfigKeyNotPresent(missing_keys, _REQUIRED_CONFIG_KEYS)

    @classmethod
    def from_file(
        cls,
        config_file_path: str,
        general: GeneralConfig,
        dependencies: list[DependencyConfig],
        template: TemplateConfig,
        git: GitConfig,
    ) -> "ConfigSchema":
        return cls(
            general=general,
            dependencies=dependencies,
            template=template,
            git=git,
            config_file_path=Path(config_file_path),
        )

    def save_on_project_folder(self) -> None:
        destination_folder = Path.cwd() / self.project_folder_name
        destination_path = destination_folder / self.config_file_path.name

        shutil.move(self.config_file_path, destination_path)

    def to_primitives(self) -> "ConfigSchemaPrimitives":
        return ConfigSchemaPrimitives(
            general=self.general.to_primitives(),
            dependencies=[dependency.to_primitives() for dependency in self.dependencies],
            template=self.template.to_primitives(),
            git=self.git.to_primitives(),
        )

    @property
    def template_type(self) -> str:
        return self.template.name

    @property
    def project_folder_name(self) -> str:
        return self.general.slug

    @property
    def dependency_manager(self) -> str:
        return self.general.dependency_manager

    @property
    def python_version(self) -> str:
        return self.general.python_version

    @property
    def version_control_has_to_be_initialized(self) -> bool:
        return self.git.initialize

    def calculate_config_destination_path(self, destination_folder: Path) -> Path:
        return destination_folder / self.project_folder_name / self.config_file_path.name


class ConfigSchemaPrimitives(TypedDict):
    general: dict[str, str]
    dependencies: list[dict[str, Union[str, bool]]]
    template: dict[str, Union[str, list[str]]]
    git: dict[str, Union[str, bool]]


class ConfigKeyNotPresent(ApplicationError):
    def __init__(self, missing_keys: list[str], required_keys: list[str]) -> None:
        super().__init__(
            message=f"The following required keys are missing from the config file: {', '.join(missing_keys)}. Required keys are: {', '.join(required_keys)}.",
            error_type=ErrorTypes.CONFIGURATION.value,
        )


class EmptyConfigurationNotAllowed(ApplicationError):
    def __init__(self) -> None:
        super().__init__(message="Configuration file cannot be empty.", error_type=ErrorTypes.CONFIGURATION.value)
