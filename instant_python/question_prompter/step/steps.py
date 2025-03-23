from abc import ABC, abstractmethod
from collections.abc import Iterator


class Step(ABC):
    @abstractmethod
    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        raise NotImplementedError


class Steps:
    def __init__(self, *step: Step) -> None:
        self._steps = list(step)

    def __iter__(self) -> Iterator[Step]:
        return iter(self._steps)
