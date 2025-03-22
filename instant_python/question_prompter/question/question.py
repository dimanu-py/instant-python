from abc import ABC, abstractmethod


class Question[T](ABC):
    def __init__(self, key: str, message: str) -> None:
        self._key = key
        self._message = message

    @abstractmethod
    def ask(self) -> T:
        raise NotImplementedError
    
    @property
    def key(self) -> str:
        return self._key
