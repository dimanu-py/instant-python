from abc import ABC, abstractmethod

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_structure import ProjectStructure


class ProjectWriter(ABC):
    @abstractmethod
    def write(self, project_structure: ProjectStructure, config: ConfigSchema) -> None:
        raise NotImplementedError
