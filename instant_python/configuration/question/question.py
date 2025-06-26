from abc import ABC, abstractmethod

from typing import TypeVar, Generic

from instant_python.configuration.question.questionary import Questionary

T = TypeVar("T")


class Question(Generic[T], ABC):
    def __init__(self, key: str, message: str, questionary: Questionary) -> None:
        self._key = key
        self._message = message
        self._questionary = questionary

    @abstractmethod
    def ask(self) -> dict[str, T]:
        raise NotImplementedError

    @property
    def key(self) -> str:
        return self._key
