from abc import ABC, abstractmethod
from typing import Union

from instant_python.config.domain.config_schema import ConfigSchema


class ConfigParser(ABC):
    @abstractmethod
    def parse(self, content: dict[str, dict], custom_config_path: Union[str, None] = None) -> ConfigSchema:
        raise NotImplementedError
