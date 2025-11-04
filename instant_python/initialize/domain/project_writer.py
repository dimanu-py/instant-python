from abc import ABC, abstractmethod
from pathlib import Path

from instant_python.initialize.domain.project_structure import ProjectStructure


class ProjectWriter(ABC):
    @abstractmethod
    def write(self, project_structure: ProjectStructure, destination: Path) -> None:
        raise NotImplementedError


class NodeWriter(ABC):
    @abstractmethod
    def create_directory(self, path: Path) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_file(self, path: Path, content: str | None = None) -> None:
        raise NotImplementedError
