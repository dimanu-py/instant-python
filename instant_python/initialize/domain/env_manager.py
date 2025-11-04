import subprocess
import sys
from abc import ABC, abstractmethod

from instant_python.config.domain.dependency_config import DependencyConfig


class EnvManager(ABC):
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory
        self._system_os = sys.platform

    @abstractmethod
    def setup(self, python_version: str, dependencies: list[DependencyConfig]) -> None:
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
