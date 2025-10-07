from abc import ABC, abstractmethod

from instant_python.config.domain.configuration_schema import ConfigurationSchema


class ConfigParser(ABC):
    @abstractmethod
    def parse(self, content: dict[str, dict]) -> ConfigurationSchema:
        raise NotImplementedError
