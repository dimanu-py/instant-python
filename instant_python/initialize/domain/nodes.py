from typing import TypeAlias, Union


class File:
    def __init__(self, name: str, extension: str, content: str | None = None) -> None:
        self._name = name
        self._extension = extension
        self._content = content

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, extension={self._extension})"

    def build_path_for(self, path: str) -> str:
        return f"{path}/{self._name}{self._extension}"


class Directory:
    def __init__(self, name: str, is_python_module: bool, children: list["Node"]) -> None:
        self._name = name
        self._is_python_module = is_python_module
        self._children = children

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, is_python_module={self._is_python_module})"

    def build_path_for(self, path: str) -> str:
        return f"{path}/{self._name}"


Node: TypeAlias = Union[File, Directory]
