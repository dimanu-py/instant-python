from abc import ABC, abstractmethod

from instant_python.config.domain.dependency_config import DependencyConfig


class EnvManager(ABC):
    @abstractmethod
    def setup(self, python_version: str, dependencies: list[DependencyConfig]) -> None:
        raise NotImplementedError
