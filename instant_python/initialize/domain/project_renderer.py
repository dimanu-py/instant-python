from abc import abstractmethod, ABC

from instant_python.config.domain.config_schema import ConfigSchema


class ProjectRenderer(ABC):
    @abstractmethod
    def render_project_structure(self, context_config: ConfigSchema, template_base_dir: str) -> list[dict]:
        raise NotImplementedError
