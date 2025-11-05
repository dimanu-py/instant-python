import subprocess

from instant_python.initialize.infra.env_manager.system_console import SystemConsole


class RuffProjectFormatter:
    def __init__(self, project_directory: str, console: SystemConsole | None = None) -> None:
        self._console = console
        self._project_directory = project_directory

    def format(self) -> None:
        self._run_command(command="uvx ruff format")

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
