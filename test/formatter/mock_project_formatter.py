from expects import expect, contain

from instant_python.formatter.project_formatter import ProjectFormatter


class MockProjectFormatter(ProjectFormatter):
    def __init__(self, project_directory: str) -> None:
        super().__init__(project_directory)
        self._commands: list[str] = []

    def _run_command(self, command: str) -> None:
        self._commands.append(command)

    def expect_to_have_been_called_with(self, command: str) -> None:
        expect(self._commands).to(contain(command))
