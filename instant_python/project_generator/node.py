from abc import ABC, abstractmethod
from pathlib import Path


class Node(ABC):
    @abstractmethod
    def create(self, base_path: Path) -> None:
        raise NotImplementedError
