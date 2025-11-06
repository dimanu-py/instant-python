from abc import ABC, abstractmethod

from instant_python.config.domain.config_schema import ConfigSchema


class ConfigRepository(ABC):
    @abstractmethod
    def read(self, path: str) -> ConfigSchema:
        raise NotImplementedError
