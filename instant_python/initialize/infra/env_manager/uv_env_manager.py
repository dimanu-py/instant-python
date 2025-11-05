import sys
from pathlib import Path

from instant_python.config.domain.dependency_config import DependencyConfig
from instant_python.initialize.domain.env_manager import EnvManager, CommandExecutionError
from instant_python.initialize.infra.env_manager.system_console import SystemConsole, CommandExecutionResult


class UvEnvManager(EnvManager):
    def __init__(self, console: SystemConsole | None = None) -> None:
        self._console = console
        self._system_os = sys.platform
        self._uv = self._set_uv_executable_based_on_os()

    def setup(self, python_version: str, dependencies: list[DependencyConfig]) -> None:
        if self._uv_is_not_installed():
            self._install()
        self._install_python(python_version)
        self._install_dependencies(dependencies)

    def _install(self) -> None:
        print(">>> Installing uv...")
        result = self._console.execute(self._get_installation_command_based_on_os())
        self._raise_command_execution_error(result)
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
        result = self._console.execute(f"{self._uv} python install {version}")
        self._raise_command_execution_error(result)
        print(f">>> Python {version} installed successfully")

    def _install_dependencies(self, dependencies: list[DependencyConfig]) -> None:
        self._create_virtual_environment()
        print(">>> Installing dependencies...")
        for dependency in dependencies:
            result = self._install_dependency(dependency)
            self._raise_command_execution_error(result)
        print(">>> Dependencies installed successfully")

    def _install_dependency(self, dependency: DependencyConfig) -> CommandExecutionResult:
        command = self._build_dependency_install_command(dependency)
        return self._console.execute(command)

    def _build_dependency_install_command(self, dependency: DependencyConfig) -> str:
        command = [f"{self._uv} add"]
        command.extend(dependency.get_installation_flag())
        command.append(dependency.get_specification())
        return " ".join(command)

    def _create_virtual_environment(self) -> None:
        result = self._console.execute(f"{self._uv} sync")
        self._raise_command_execution_error(result)

    def _uv_is_not_installed(self) -> bool:
        result = self._console.execute(f"{self._uv} --version")
        return not result.success()

    @staticmethod
    def _raise_command_execution_error(result: CommandExecutionResult) -> None:
        if not result.success():
            raise CommandExecutionError(exit_code=result.exit_code, stderr_output=result.stderr)
