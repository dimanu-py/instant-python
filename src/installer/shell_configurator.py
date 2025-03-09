from abc import ABC, abstractmethod


class ShellConfigurator(ABC):
    @abstractmethod
    def configure(self) -> None:
        raise NotImplementedError
