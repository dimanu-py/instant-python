from pathlib import Path

from test.project_creator.directory_mother import DirectoryMother


class TestDirectory:
    def teardown_method(self) -> None:
        directory = Path(__file__).parent / "value_objects"
        if directory.exists():
            for item in directory.iterdir():
                if item.is_file():
                    item.unlink()
            directory.rmdir()

    def test_should_create_normal_directory(self) -> None:
        directory = DirectoryMother.any()

        directory.create(base_path=Path(__file__).parent)

        assert (Path(__file__).parent / directory._name).exists()

    def test_should_create_python_directory_with_init_file(self) -> None:
        directory = DirectoryMother.as_python()

        directory.create(base_path=Path(__file__).parent)

        directory_name = Path(__file__).parent / directory._name
        assert directory_name.exists()
        assert (directory_name / "__init__.py").exists()

    def test_should_create_directory_with_other_directory_inside(self) -> None:
        inner_directory = DirectoryMother.any()
        directory = DirectoryMother.with_children(inner_directory)

        directory.create(base_path=Path(__file__).parent)

        directory_name = (Path(__file__).parent / directory._name)
        assert directory_name.exists()
        assert (directory_name / inner_directory._name).exists()
