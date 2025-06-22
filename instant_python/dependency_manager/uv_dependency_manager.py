import subprocess

from instant_python.configuration.dependency.dependency_configuration import DependencyConfiguration
from instant_python.dependency_manager.dependency_manager import DependencyManager
from instant_python.errors.command_execution_error import CommandExecutionError


class UvDependencyManager(DependencyManager):
    def __init__(self, project_directory: str) -> None:
        super().__init__(project_directory)
        self._uv = "~/.local/bin/uv"

    def setup_environment(self, python_version: str, dependencies: list[DependencyConfiguration]) -> None:
        try:
            self._install()
            self._install_python(python_version)
            self._install_dependencies(dependencies)
        except subprocess.CalledProcessError as error:
            raise CommandExecutionError(exit_code=error.returncode, stderr_output=error.stderr)

    def _install(self) -> None:
        print(">>> Installing uv...")
        self._run_command(command="curl -LsSf https://astral.sh/uv/install.sh | sh")
        print(">>> uv installed successfully")

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
            print(f">>> Dependency {dependency['name']} installed successfully")

    def _build_dependency_install_command(self, dependency: dict[str, str]) -> str:
        name = dependency["name"]
        version = dependency["version"]
        is_dev = dependency.get("is_dev", False)
        group = dependency.get("group", None)

        command = [f"{self._uv} add"]

        if (is_dev and group) or group:
            command.append(f"--group {group}")
        elif is_dev:
            command.append("--dev")

        dependency_spec = name if version == "latest" else f"{name}=={version}"
        command.append(dependency_spec)

        return " ".join(command)

    def _create_virtual_environment(self) -> None:
        self._run_command(f"{self._uv} sync")
