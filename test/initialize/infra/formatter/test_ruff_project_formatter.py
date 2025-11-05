import os

from test.initialize.infra.formatter.mock_project_formatter import MockRuffProjectFormatter


class TestRuffProjectFormatter:
    def setup_method(self) -> None:
        self._formatter = MockRuffProjectFormatter(project_directory=os.getcwd())

    def test_should_format_project_files(self) -> None:
        self._formatter.format()

        self._formatter.expect_to_have_been_called_with("uvx ruff format")
