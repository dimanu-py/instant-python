from abc import ABC, abstractmethod

from instant_python.config.domain.configuration_schema import ConfigurationSchema


class YamlWriter(ABC):
    @abstractmethod
    def write(self, configuration: ConfigurationSchema) -> None:
        raise NotImplementedError
