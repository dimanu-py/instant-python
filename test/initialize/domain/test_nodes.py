from pathlib import Path

from doublex import Spy
from doublex_expects import have_been_called_with
from expects import expect, equal

from instant_python.initialize.domain.project_writer import NodeWriter
from instant_python.initialize.domain.nodes import File, Directory


class TestFile:
    def test_should_build_file_path_inside_project(self) -> None:
        file = File(name="sample", extension=".py", content="")

        path = file.build_path_for(path=Path("my_project"))

        expect(str(path)).to(equal("my_project/sample.py"))

    def test_should_create_empty_file(self) -> None:
        file = File(name="sample", extension=".py", content="")
        file_writer = Spy(NodeWriter)

        file.create(writer=file_writer, destination=Path("my_project"))

        expect(file_writer.create_file).to(have_been_called_with(Path("my_project/sample.py"), ""))

class TestDirectory:
    def test_should_build_directory_path_inside_project(self) -> None:
        directory = Directory(name="config", is_python_module=True, children=[])

        path = directory.build_path_for(path=Path("my_project"))

        expect(str(path)).to(equal("my_project/config"))
