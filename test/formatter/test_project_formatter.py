import os

from test.formatter.mock_project_formatter import MockProjectFormatter


class TestProjectFormatter:
    def setup_method(self) -> None:
        self._formatter = MockProjectFormatter(project_directory=os.getcwd())

    def test_should_format_project_files(self) -> None:
        self._formatter.format()

        self._formatter.expect_to_have_been_called_with("uvx ruff format")
