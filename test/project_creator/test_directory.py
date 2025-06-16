import shutil
from pathlib import Path

from expects import be_true, expect

from instant_python.project_creator.file import File
from test.project_creator.directory_mother import DirectoryMother


class TestDirectory:
    def teardown_method(self) -> None:
        for item in Path(__file__).parent.iterdir():
            if item.is_dir() and item.name.startswith("test_dir_"):
                shutil.rmtree(item)

    def test_should_create_normal_directory(self) -> None:
        directory = DirectoryMother.any()

        directory.create(base_path=Path(__file__).parent)

        expect((Path(__file__).parent / directory._name).exists()).to(be_true)

    def test_should_create_python_directory_with_init_file(self) -> None:
        directory = DirectoryMother.as_python()

        directory.create(base_path=Path(__file__).parent)

        directory_name = Path(__file__).parent / directory._name
        expect(directory_name.exists()).to(be_true)
        expect((directory_name / "__init__.py").exists()).to(be_true)

    def test_should_create_directory_with_other_directory_inside(self) -> None:
        inner_directory = DirectoryMother.any()
        directory = DirectoryMother.with_children(inner_directory)

        directory.create(base_path=Path(__file__).parent)

        directory_name = Path(__file__).parent / directory._name
        expect(directory_name.exists()).to(be_true)
        expect((directory_name / inner_directory._name).exists()).to(be_true)

    def test_should_create_directory_with_file_inside(self) -> None:
        file = File(name="domain_error", extension=".py")
        directory = DirectoryMother.with_children(file)

        directory.create(base_path=Path(__file__).parent)

        directory_name = Path(__file__).parent / directory._name
        expect(directory_name.exists()).to(be_true)
        expect((directory_name / "domain_error.py").exists()).to(be_true)
