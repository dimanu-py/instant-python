import subprocess
import sys
from abc import ABC, abstractmethod

from instant_python.config.domain.dependency_config import DependencyConfig
from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


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


class CommandExecutionError(ApplicationError):
    def __init__(self, exit_code: int, stderr_output: str = None) -> None:
        message = f"Unexpected error when executing a command, exit code {exit_code}"
        if stderr_output:
            message += f": {stderr_output.decode('utf-8').strip()}"
        super().__init__(message=message, error_type=ErrorTypes.INSTALLER.value)
