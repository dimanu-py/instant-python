from abc import ABC, abstractmethod
from enum import StrEnum
from pathlib import Path


class NodeType(StrEnum):
    PYTHON_MODULE = "python-module"
    PYTHON_FILE = "python-file"


class Node(ABC):
    @abstractmethod
    def create(self, base_path: Path) -> None:
        raise NotImplementedError
