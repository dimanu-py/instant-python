from dataclasses import dataclass, field

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
    dependencies: list[DependencyConfiguration] = field(init=False)
    template: TemplateConfiguration = field(init=False)
    git: GitConfiguration = field(init=False)

    def to_primitives(self) -> dict[str, dict]:
        return {
            "general": self.general.to_primitives(),
            "dependencies": [
                dependency.to_primitives() for dependency in self.dependencies
            ],
            "template": self.template.to_primitives(),
            "git": self.git.to_primitives(),
        }
