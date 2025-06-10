from pathlib import Path

from instant_python.project_creator.directory import Directory


class TestDirectory:
    def teardown_method(self) -> None:
        directory = Path(__file__).parent / "value_objects"
        if directory.exists():
            directory.rmdir()

    def test_should_create_normal_directory(self) -> None:
        directory = Directory(name="value_objects", children=[], is_python=False)

        directory.create(base_path=Path(__file__).parent)

        assert (Path(__file__).parent / "value_objects").exists()
