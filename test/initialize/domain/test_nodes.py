from pathlib import Path

from expects import expect, equal

from instant_python.initialize.domain.nodes import File, Directory


class TestFile:
    def test_should_build_file_path_inside_project(self) -> None:
        file = File(name="sample", extension=".py", content="")

        path = file.build_path_for(path=Path("my_project"))

        expect(str(path)).to(equal("my_project/sample.py"))


class TestDirectory:
    def test_should_build_directory_path_inside_project(self) -> None:
        directory = Directory(name="config", is_python_module=True, children=[])

        path = directory.build_path_for(path=Path("my_project"))

        expect(str(path)).to(equal("my_project/config"))
