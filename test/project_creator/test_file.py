from pathlib import Path

from instant_python.project_creator.file import File


class TestFile:
    def teardown_method(self) -> None:
        file_path = Path(__file__).parent / "domain_error.py"

        if file_path.exists():
            file_path.unlink()

    def test_should_extract_file_name(self) -> None:
        file = File(name="exceptions/domain_error", extension=".py")

        assert file._file_name == "domain_error.py"

    def test_should_create_file_at_specified_path(self) -> None:
        file = File(name="exceptions/domain_error", extension=".py")

        file.create(base_path=Path(__file__).parent)

        file_path = Path(__file__).parent / "domain_error.py"
        assert file_path.exists()
