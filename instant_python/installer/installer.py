import subprocess

from instant_python.errors.command_execution_error import CommandExecutionError
from instant_python.installer.dependency_manager import DependencyManager


class Installer:
    _dependency_manager: DependencyManager

    def __init__(
        self,
        dependency_manager: DependencyManager,
    ) -> None:
        self._dependency_manager = dependency_manager

    def perform_installation(
        self, python_version: str, dependencies: list[str]
    ) -> None:
        try:
            self._dependency_manager.install()
            self._dependency_manager.install_python(python_version)
            self._dependency_manager.install_dependencies(dependencies)
        except subprocess.CalledProcessError as error:
            raise CommandExecutionError(
                exit_code=error.returncode, stderr_output=error.stderr
            )
