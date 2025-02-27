from abc import ABC, abstractmethod
from enum import StrEnum
from pathlib import Path


class NodeType(StrEnum):
    DIRECTORY = "directory"
    FILE = "file"


class Node(ABC):
    @abstractmethod
    def create(self, base_path: Path) -> None:
        raise NotImplementedError
