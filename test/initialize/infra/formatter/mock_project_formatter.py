from expects import expect, contain

from instant_python.initialize.infra.formatter.ruff_project_formatter import RuffProjectFormatter


class MockRuffProjectFormatter(RuffProjectFormatter):
    def __init__(self, project_directory: str) -> None:
        super().__init__(project_directory)
        self._commands: list[str] = []

    def _run_command(self, command: str) -> None:
        self._commands.append(command)

    def expect_to_have_been_called_with(self, command: str) -> None:
        expect(self._commands).to(contain(command))
