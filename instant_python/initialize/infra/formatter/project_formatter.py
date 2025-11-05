import subprocess


class ProjectFormatter:
    def __init__(self, project_directory: str) -> None:
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
