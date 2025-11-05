import os

from doublex import Mock, Mimic, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, raise_error

from instant_python.initialize.domain.env_manager import CommandExecutionError
from instant_python.initialize.infra.env_manager.system_console import SystemConsole
from test.initialize.infra.env_manager.mother.command_execution_result_mother import CommandExecutionResultMother
from test.initialize.infra.formatter.mock_project_formatter import MockRuffProjectFormatter
from instant_python.initialize.infra.formatter.ruff_project_formatter import RuffProjectFormatter


class TestRuffProjectFormatter:
    def setup_method(self) -> None:
        self._console = Mimic(Mock, SystemConsole)
        self._formatter = MockRuffProjectFormatter(project_directory=os.getcwd())
        self._ruff_formatter = RuffProjectFormatter(project_directory=os.getcwd(), console=self._console)

    def test_should_execute_ruff_formatter(self) -> None:
        expect_call(self._console).execute("uvx ruff format").returns(CommandExecutionResultMother.success())

        self._ruff_formatter.format()

        expect(self._console).to(have_been_satisfied)

    def test_should_raise_error_if_format_command_fails(self) -> None:
        expect_call(self._console).execute("uvx ruff format").returns(CommandExecutionResultMother.failure())

        expect(lambda: self._ruff_formatter.format()).to(raise_error(CommandExecutionError))

    def test_should_format_project_files(self) -> None:
        self._formatter.format()

        self._formatter.expect_to_have_been_called_with("uvx ruff format")
