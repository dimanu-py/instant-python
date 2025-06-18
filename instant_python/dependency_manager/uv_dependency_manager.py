import subprocess


class UvDependencyManager:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

    def _install(self) -> None:
        print(">>> Installing uv...")
        self._run_command(command="curl -LsSf https://astral.sh/uv/install.sh | sh")
        print(">>> uv installed successfully")

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
