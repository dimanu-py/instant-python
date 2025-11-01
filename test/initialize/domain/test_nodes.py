from expects import expect, equal

from instant_python.initialize.domain.nodes import File


class TestFile:
    def test_should_build_file_path_inside_project(self) -> None:
        file = File(name="sample", extension=".py", content="")

        path = file.build_path_for(path="my_project")

        expect(path).to(equal("my_project/sample.py"))
