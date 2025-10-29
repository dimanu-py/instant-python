from abc import abstractmethod, ABC

from instant_python.config.domain.config_schema import ConfigSchema


class ProjectRenderer(ABC):
    @abstractmethod
    def render(self, context_config: ConfigSchema) -> list[dict]:
        raise NotImplementedError
