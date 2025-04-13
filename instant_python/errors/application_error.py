from abc import ABC, abstractmethod


class ApplicationError(Exception, ABC):
    @property
    @abstractmethod
    def type(self) -> str: ...

    @property
    @abstractmethod
    def message(self) -> str: ...
