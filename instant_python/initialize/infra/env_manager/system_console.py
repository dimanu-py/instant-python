from dataclasses import dataclass


@dataclass(frozen=True)
class CommandExecutionResult:
    exit_code: int
    stdout: str
    stderr: str


class SystemConsole:
    def __init__(self, working_directory: str) -> None:
        self._working_directory = working_directory

    def execute(self, command: str) -> CommandExecutionResult:
        raise NotImplementedError
