from abc import ABC, abstractmethod
from typing import Union

from instant_python.config.domain.configuration_schema import ConfigurationSchema


class ConfigParser(ABC):
    @abstractmethod
    def parse(self, content: dict[str, dict], custom_config_path: Union[str, None] = None) -> ConfigurationSchema:
        raise NotImplementedError
