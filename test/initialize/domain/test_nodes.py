from pathlib import Path

from doublex import Spy
from doublex_expects import have_been_called_with, have_been_called
from expects import expect, equal

from instant_python.initialize.domain.project_writer import NodeWriter
from instant_python.initialize.domain.nodes import File, Directory


class TestFile:
    _EMPTY_CONTENT = ""
    _SOME_CONTENT = "print('Hello, World!')"
    _SOME_PROJECT_PATH = Path("my_project")
    _SOME_NAME = "sample"
    _SOME_EXTENSION = ".py"

    def setup_method(self) -> None:
        self._file_writer = Spy(NodeWriter)

    def test_should_create_empty_file(self) -> None:
        file = File(name=self._SOME_NAME, extension=self._SOME_EXTENSION, content=self._EMPTY_CONTENT)

        file.create(writer=self._file_writer, destination=self._SOME_PROJECT_PATH)

        expect(self._file_writer.create_file).to(have_been_called_with(Path("my_project/sample.py"), self._EMPTY_CONTENT))

    def test_should_create_file_with_content(self) -> None:
        file = File(name=self._SOME_NAME, extension=self._SOME_EXTENSION, content=self._SOME_CONTENT)

        file.create(writer=self._file_writer, destination=self._SOME_PROJECT_PATH)

        expect(self._file_writer.create_file).to(have_been_called_with(Path("my_project/sample.py"), self._SOME_CONTENT))


class TestDirectory:
    def test_should_build_directory_path_inside_project(self) -> None:
        directory = Directory(name="config", is_python_module=True, children=[])

        path = directory.build_path_for(path=Path("my_project"))

        expect(str(path)).to(equal("my_project/config"))

    def test_should_create_empty_directory(self) -> None:
        directory = Directory(name="docs", is_python_module=False, children=[])
        directory_writer = Spy(NodeWriter)

        directory.create(writer=directory_writer, destination=Path("my_project"))

        expect(directory_writer.create_directory).to(have_been_called_with(Path("my_project/docs")))
        expect(directory_writer.create_file).to_not(have_been_called)
