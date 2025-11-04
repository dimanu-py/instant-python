import subprocess
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
        return self._run_command(command)

    def _run_command(self, command: str) -> CommandExecutionResult:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            cwd=self._working_directory,
            capture_output=True,
            text=True,
        )
        return CommandExecutionResult(
            exit_code=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
        )
