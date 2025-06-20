import subprocess

from instant_python.errors.command_execution_error import CommandExecutionError


class UvDependencyManager:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory
        self._uv = "~/.local/bin/uv"

    def setup_environment(self, python_version: str, dependencies: list[dict]) -> None:
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

    def _install_dependencies(self, dependencies: list[dict]) -> None:
        self._create_virtual_environment()
        print(">>> Installing dependencies...")
        for dependency in dependencies:
            command = self._build_dependency_install_command(dependency)
            self._run_command(command)
            print(f">>> Dependency {dependency} installed successfully")

    def _build_dependency_install_command(self, dependency: dict[str, str]) -> str:
        name = dependency["name"]
        version = dependency["version"]
        is_dev = dependency.get("is_dev", False)
        group = dependency.get("group", None)

        command = [f"{self._uv} add"]

        if is_dev:
            command.append("--dev")
        if group:
            command.append(f"--group {group}")

        dependency_spec = name if version == "latest" else f"{name}=={version}"
        command.append(dependency_spec)

        return " ".join(command)

    def _create_virtual_environment(self) -> None:
        self._run_command(f"{self._uv} sync")

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
