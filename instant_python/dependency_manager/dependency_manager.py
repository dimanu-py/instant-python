import subprocess
from abc import ABC, abstractmethod
import sys

from instant_python.configuration.dependency.dependency_configuration import DependencyConfiguration


class DependencyManager(ABC):
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory
        self._system_os = sys.platform

    @abstractmethod
    def setup_environment(self, python_version: str, dependencies: list[DependencyConfiguration]) -> None:
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
