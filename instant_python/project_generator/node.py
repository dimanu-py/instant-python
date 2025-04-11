from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path


class NodeType(str, Enum):
    DIRECTORY = "directory"
    FILE = "file"
    BOILERPLATE = "boilerplate_file"


class Node(ABC):
    @abstractmethod
    def create(self, base_path: Path) -> None:
        raise NotImplementedError
