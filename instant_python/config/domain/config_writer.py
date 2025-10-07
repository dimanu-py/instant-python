from abc import ABC, abstractmethod

from instant_python.config.domain.configuration_schema import ConfigurationSchema


class ConfigWriter(ABC):
    @abstractmethod
    def write(self, configuration: ConfigurationSchema) -> None:
        raise NotImplementedError
