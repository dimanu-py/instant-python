from instant_python.initialize.domain.nodes import File, Directory, Node
from test.random_generator import RandomGenerator


class FileMother:
    _EMPTY_CONTENT = ""
    _PYTHON_EXTENSION = ".py"

    @classmethod
    def empty(cls) -> File:
        return File(
            name=RandomGenerator.word(),
            extension=cls._PYTHON_EXTENSION,
            content=cls._EMPTY_CONTENT,
        )


class DirectoryMother:
    _PYTHON_MODULE = True
    _EMPTY = []

    @classmethod
    def without_children(cls) -> Directory:
        return Directory(
            name=RandomGenerator.word(),
            is_python_module=cls._PYTHON_MODULE,
            children=cls._EMPTY,
        )

    @classmethod
    def with_children(cls, children: list[Node]) -> Directory:
        return Directory(
            name=RandomGenerator.word(),
            is_python_module=cls._PYTHON_MODULE,
            children=children,
        )
