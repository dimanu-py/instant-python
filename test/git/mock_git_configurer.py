from expects import expect, be_empty, contain

from instant_python.git.git_configurer import GitConfigurer


class MockGitConfigurer(GitConfigurer):
    def __init__(self, project_directory: str) -> None:
        super().__init__(project_directory=project_directory)
        self._commands = []

    def expect_to_not_have_initialized_repository(self) -> None:
        expect(self._commands).to(be_empty)

    def expect_to_have_been_called_with(self, *commands: str) -> None:
        for command in commands:
            expect(self._commands).to(contain(command))

    def _run_command(self, command: str) -> None:
        self._commands.append(command)
