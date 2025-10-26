from abc import ABC, abstractmethod

from instant_python.config.domain.config_schema import ConfigSchema


class ConfigWriter(ABC):
    @abstractmethod
    def write(self, config: ConfigSchema) -> None:
        raise NotImplementedError
