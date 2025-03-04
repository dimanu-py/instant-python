from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Question[T](ABC):
    key: str
    message: str
    default: str = field(default_factory=str)
    multiselect: bool = field(default=False)

    @abstractmethod
    def ask(self) -> T:
        raise NotImplementedError
