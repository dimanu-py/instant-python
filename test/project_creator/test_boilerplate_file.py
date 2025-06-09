from pathlib import Path

from instant_python.project_creator.boilerplate_file import BoilerplateFile


class TestBoilerplateFile:
    def test_should_extract_file_name(self) -> None:
        file = BoilerplateFile(name="exceptions/domain_error", extension=".py")

        assert file._file_name == "domain_error.py"

    def test_should_create_file_at_specified_file(self) -> None:
        file = BoilerplateFile(name="exceptions/domain_error", extension=".py")

        file.create(base_path=Path(__file__).parent)

        file_path = Path(__file__).parent / "domain_error.py"
        assert file_path.exists()
