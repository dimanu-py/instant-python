import subprocess

from instant_python.initialize.domain.env_manager import CommandExecutionError
from instant_python.initialize.infra.env_manager.system_console import SystemConsole


class RuffProjectFormatter:
    def __init__(self, project_directory: str, console: SystemConsole | None = None) -> None:
        self._console = console
        self._project_directory = project_directory

    def format(self) -> None:
        if self._console is None:
            self._run_command(command="uvx ruff format")
        else:
            result = self._console.execute(command="uvx ruff format")
            if not result.success():
                raise CommandExecutionError(
                    exit_code=result.exit_code,
                    stderr_output=result.stderr,
                )

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
