from abc import ABC, abstractmethod
from pathlib import Path

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_structure import ProjectStructure


class ProjectWriter(ABC):
    @abstractmethod
    def write(self, project_structure: ProjectStructure, config: ConfigSchema, destination: Path) -> None:
        raise NotImplementedError
