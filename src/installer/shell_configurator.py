from abc import ABC, abstractmethod


class ShellConfigurator(ABC):
    @abstractmethod
    def configure_shell_completion(self) -> None:
        raise NotImplementedError
