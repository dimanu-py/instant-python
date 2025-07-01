from pathlib import Path
import subprocess

from instant_python.configuration.dependency.dependency_configuration import DependencyConfiguration
from instant_python.dependency_manager.dependency_manager import DependencyManager
from instant_python.dependency_manager.command_execution_error import CommandExecutionError


class PdmDependencyManager(DependencyManager):
    def __init__(self, project_directory: str) -> None:
        super().__init__(project_directory)
        self._pdm = self._set_pdm_executable_based_on_os()

    def setup_environment(self, python_version: str, dependencies: list[DependencyConfiguration]) -> None:
        try:
            self._install()
            self._install_python(python_version)
            self._install_dependencies(dependencies)
        except subprocess.CalledProcessError as error:
            raise CommandExecutionError(exit_code=error.returncode, stderr_output=error.stderr)

    def _install(self) -> None:
        print(">>> Installing pdm...")
        self._run_command(command=self._get_installation_command_based_on_os())
        print(">>> pdm installed successfully")

    def _set_pdm_executable_based_on_os(self):
        return (
            f"{str(Path.home() / 'AppData' / 'Roaming' / 'Python' / 'Scripts' / 'pdm.exe')}"
            if self._system_os.startswith("win")
            else "~/.local/bin/pdm"
        )

    def _get_installation_command_based_on_os(self) -> str:
        if self._system_os.startswith("win"):
            return 'powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"'
        return "curl -sSL https://pdm-project.org/install-pdm.py | python3 -"

    def _install_python(self, version: str) -> None:
        print(f">>> Installing Python {version}...")
        self._run_command(command=f"{self._pdm} python install {version}")
        print(f">>> Python {version} installed successfully")

    def _install_dependencies(self, dependencies: list[DependencyConfiguration]) -> None:
        self._create_virtual_environment()
        print(">>> Installing dependencies...")
        for dependency in dependencies:
            command = self._build_dependency_install_command(dependency)
            self._run_command(command)
        print(">>> Dependencies installed successfully")

    def _build_dependency_install_command(self, dependency: DependencyConfiguration) -> str:
        command = [f"{self._pdm} add"]
        command.extend(dependency.get_installation_flag())
        command.append(dependency.get_specification())

        return " ".join(command)

    def _create_virtual_environment(self) -> None:
        self._run_command(f"{self._pdm} install")
