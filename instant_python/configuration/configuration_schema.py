import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import TypedDict, Union

import yaml

from instant_python.configuration.dependency.dependency_configuration import (
    DependencyConfiguration,
)
from instant_python.configuration.general.general_configuration import (
    GeneralConfiguration,
)
from instant_python.configuration.git.git_configuration import GitConfiguration
from instant_python.configuration.template.template_configuration import (
    TemplateConfiguration,
)


@dataclass
class ConfigurationSchema:
    general: GeneralConfiguration
    dependencies: list[DependencyConfiguration]
    template: TemplateConfiguration
    git: GitConfiguration
    _config_file_path: Path = field(default_factory=lambda: Path("ipy.yml"))

    @classmethod
    def from_file(
        cls,
        config_file_path: str,
        general: GeneralConfiguration,
        dependencies: list[DependencyConfiguration],
        template: TemplateConfiguration,
        git: GitConfiguration,
    ) -> "ConfigurationSchema":
        return cls(
            general=general,
            dependencies=dependencies,
            template=template,
            git=git,
            _config_file_path=Path(config_file_path),
        )

    def save_on_project_folder(self) -> None:
        destination_folder = Path.cwd() / self.project_folder_name
        destination_path = destination_folder / self._config_file_path.name

        shutil.move(self._config_file_path, destination_path)

    def save_on_current_directory(self) -> None:
        destination_folder = Path.cwd() / self._config_file_path
        with open(destination_folder, "w") as file:
            yaml.dump(self.to_primitives(), file)

    def to_primitives(self) -> "ConfigurationSchemaPrimitives":
        return ConfigurationSchemaPrimitives(
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


class ConfigurationSchemaPrimitives(TypedDict):
    general: dict[str, str]
    dependencies: list[dict[str, Union[str, bool]]]
    template: dict[str, Union[str, list[str]]]
    git: dict[str, Union[str, bool]]
