import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import TypedDict, Union

import yaml

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


@dataclass
class ConfigSchema:
    general: GeneralConfig
    dependencies: list[DependencyConfig]
    template: TemplateConfig
    git: GitConfig
    config_file_path: Path = field(default_factory=lambda: Path("ipy.yml"))

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


class ConfigSchemaPrimitives(TypedDict):
    general: dict[str, str]
    dependencies: list[dict[str, Union[str, bool]]]
    template: dict[str, Union[str, list[str]]]
    git: dict[str, Union[str, bool]]
