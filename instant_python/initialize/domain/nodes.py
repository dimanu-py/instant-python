from collections.abc import Iterator
from enum import Enum
from pathlib import Path
from typing import TypeAlias, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from instant_python.initialize.domain.project_writer import NodeWriter


class File:
    def __init__(self, name: str, extension: str, content: str | None = None) -> None:
        self._name = name
        self._extension = extension
        self._content = content

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, extension={self._extension})"

    def create(self, writer: "NodeWriter", destination: Path) -> None:
        file_path = self._build_path_for(destination)
        writer.create_file(file_path, self._content)

    def is_empty(self) -> bool:
        return self._content is None or self._content == ""

    def _build_path_for(self, path: Path) -> Path:
        return path / f"{self._name}{self._extension}"


class Directory:
    def __init__(self, name: str, is_python_module: bool, children: list["Node"]) -> None:
        self._name = name
        self._is_python_module = is_python_module
        self._children = children

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, is_python_module={self._is_python_module})"

    def __iter__(self) -> Iterator["Node"]:
        return iter(self._children)

    def create(self, writer: "NodeWriter", destination: Path) -> None:
        directory_path = self._build_path_for(destination)
        writer.create_directory(directory_path)

    def _build_path_for(self, path: Path) -> Path:
        return path / self._name


class NodeType(str, Enum):
    DIRECTORY = "directory"
    FILE = "file"


Node: TypeAlias = Union[File, Directory]
