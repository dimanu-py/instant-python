from abc import ABC, abstractmethod
from pathlib import Path

from instant_python.shared.domain.config_schema import ConfigSchema


class ConfigRepository(ABC):
    @abstractmethod
    def read(self, path: Path) -> ConfigSchema:
        raise NotImplementedError

    @abstractmethod
    def move(self, config: ConfigSchema, destination_path: Path) -> None:
        raise NotImplementedError
