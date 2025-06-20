import subprocess
from abc import ABC, abstractmethod


class DependencyManager(ABC):
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

    @abstractmethod
    def setup_environment(self, python_version: str, dependencies: list[dict]) -> None:
        raise NotImplementedError

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
