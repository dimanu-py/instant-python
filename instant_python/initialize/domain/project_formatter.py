from abc import ABC, abstractmethod


class ProjectFormatter(ABC):
    @abstractmethod
    def format(self) -> None:
        raise NotImplementedError
