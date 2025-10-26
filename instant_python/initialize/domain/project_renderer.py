from abc import abstractmethod, ABC

from instant_python.config.domain.configuration_schema import ConfigurationSchema


class ProjectRenderer(ABC):
    @abstractmethod
    def render_project_structure(self, context_config: ConfigurationSchema, template_base_dir: str) -> list[dict]:
        raise NotImplementedError
