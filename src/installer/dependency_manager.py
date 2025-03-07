from abc import ABC, abstractmethod


class DependencyManager(ABC):
    @abstractmethod
    def install(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def install_python(self, version: str) -> None:
        raise NotImplementedError
