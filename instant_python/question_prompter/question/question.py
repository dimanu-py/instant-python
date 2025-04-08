from abc import ABC, abstractmethod

from typing import TypeVar, Generic

T = TypeVar("T")

class Question(Generic[T], ABC):
    def __init__(self, key: str, message: str) -> None:
        self._key = key
        self._message = message

    @abstractmethod
    def ask(self) -> dict[str, T]:
        raise NotImplementedError
    
    @property
    def key(self) -> str:
        return self._key
