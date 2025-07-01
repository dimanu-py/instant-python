from pathlib import Path
import subprocess

from instant_python.configuration.dependency.dependency_configuration import DependencyConfiguration
from instant_python.dependency_manager.dependency_manager import DependencyManager
from instant_python.dependency_manager.command_execution_error import CommandExecutionError


class UvDependencyManager(DependencyManager):
    def __init__(self, project_directory: str) -> None:
        super().__init__(project_directory)
        self._uv = self._set_uv_executable_based_on_os()

    def setup_environment(self, python_version: str, dependencies: list[DependencyConfiguration]) -> None:
        try:
            self._install()
            self._install_python(python_version)
            self._install_dependencies(dependencies)
        except subprocess.CalledProcessError as error:
            raise CommandExecutionError(exit_code=error.returncode, stderr_output=error.stderr)

    def _install(self) -> None:
        print(">>> Installing uv...")
        self._run_command(command=self._get_installation_command_based_on_os())
        print(">>> uv installed successfully")
        if self._system_os.startswith("win"):
            print(
                ">>> Remember to add uv to your PATH environment variable. You can do this:\n"
                "    1. Running the following command if you use cmd:\n"
                "       set Path=%Path%;%USERPROFILE%\\.local\\bin\n"
                "    2. Running the following command if you use PowerShell:\n"
                "       $env:Path = '$env:USERPROFILE\\.local\\bin;$env:Path'\n"
                "    3. Restarting your shell."
            )

    def _get_installation_command_based_on_os(self) -> str:
        if self._system_os.startswith("win"):
            return 'powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"'
        return "curl -LsSf https://astral.sh/uv/install.sh | sh"

    def _set_uv_executable_based_on_os(self):
        return (
            f"{str(Path.home() / '.local' / 'bin' / 'uv.exe')}"
            if self._system_os.startswith("win")
            else "~/.local/bin/uv"
        )

    def _install_python(self, version: str) -> None:
        print(f">>> Installing Python {version}...")
        self._run_command(command=f"{self._uv} python install {version}")
        print(f">>> Python {version} installed successfully")

    def _install_dependencies(self, dependencies: list[DependencyConfiguration]) -> None:
        self._create_virtual_environment()
        print(">>> Installing dependencies...")
        for dependency in dependencies:
            command = self._build_dependency_install_command(dependency)
            self._run_command(command)
        print(">>> Dependencies installed successfully")

    def _build_dependency_install_command(self, dependency: DependencyConfiguration) -> str:
        command = [f"{self._uv} add"]
        command.extend(dependency.get_installation_flag())
        command.append(dependency.get_specification())
        return " ".join(command)

    def _create_virtual_environment(self) -> None:
        self._run_command(f"{self._uv} sync")
