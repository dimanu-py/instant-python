from pathlib import Path

from instant_python.project_creator.directory import Directory


class TestDirectory:
    def teardown_method(self) -> None:
        directory = Path(__file__).parent / "value_objects"
        if directory.exists():
            for item in directory.iterdir():
                if item.is_file():
                    item.unlink()
            directory.rmdir()

    def test_should_create_normal_directory(self) -> None:
        directory = Directory(name="value_objects", is_python=False)

        directory.create(base_path=Path(__file__).parent)

        assert (Path(__file__).parent / "value_objects").exists()

    def test_should_create_python_directory_with_init_file(self) -> None:
        directory = Directory(name="value_objects", is_python=True)

        directory.create(base_path=Path(__file__).parent)

        assert (Path(__file__).parent / "value_objects").exists()
        assert (Path(__file__).parent / "value_objects" / "__init__.py").exists()
