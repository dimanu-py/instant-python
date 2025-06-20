from abc import ABC, abstractmethod


class DependencyManager(ABC):

    @abstractmethod
    def setup_environment(self, python_version: str, dependencies: list[dict]) -> None:
        raise NotImplementedError
