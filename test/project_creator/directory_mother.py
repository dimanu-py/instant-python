from instant_python.project_creator.directory import Directory
from instant_python.project_creator.node import Node
from test.random_generator import RandomGenerator


class DirectoryMother:
    _TEST_DIR_PREFIX = "test_dir_"

    @classmethod
    def any(cls) -> Directory:
        return Directory(
            name=f"{cls._TEST_DIR_PREFIX}{RandomGenerator.name()}",
            is_python=False,
            children=[],
        )

    @classmethod
    def as_python(cls) -> Directory:
        return Directory(
            name=f"{cls._TEST_DIR_PREFIX}{RandomGenerator.name()}",
            is_python=True,
            children=[],
        )

    @classmethod
    def with_children(cls, *children: Node) -> Directory:
        return Directory(
            name=f"{cls._TEST_DIR_PREFIX}{RandomGenerator.name()}",
            is_python=False,
            children=list(children),
        )
