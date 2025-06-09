from instant_python.project_creator.boilerplate_file import BoilerplateFile


class TestBoilerplateFile:
    def test_should_extract_file_name(self) -> None:
        file = BoilerplateFile(name="exceptions/domain_error", extension=".py")

        assert file._file_name == "domain_error.py"
