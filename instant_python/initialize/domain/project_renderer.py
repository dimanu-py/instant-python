from abc import abstractmethod, ABC

from instant_python.shared.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_structure import ProjectStructure


class ProjectRenderer(ABC):
    @abstractmethod
    def render(self, context_config: ConfigSchema) -> ProjectStructure:
        raise NotImplementedError
