import subprocess

from instant_python.errors.command_execution_error import CommandExecutionError


class UvDependencyManager:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

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
        self._run_command(command=f"~/.local/bin/uv python install {version}")
        print(f">>> Python {version} installed successfully")

    def _install_dependencies(self, dependencies: list[dict]) -> None:
        self._create_virtual_environment()
        for dependency in dependencies:
            command = self._build_dependency_install_command(dependency)
            self._run_command(command)

    def _build_dependency_install_command(self, dependency: dict[str, str]) -> str:
        name = dependency["name"]
        version = dependency["version"]
        is_dev = dependency.get("is_dev", False)
        group = dependency.get("group", None)
        flag = "--dev" if is_dev else None
        if group:
            flag = f"{flag} --group {group}"
        dependency_name = f"{name}=={version}" if version != "latest" else name
        command = f"~/.local/bin/uv add {flag} {dependency_name}" if flag else f"~/.local/bin/uv add {dependency_name}"
        return command

    def _create_virtual_environment(self) -> None:
        self._run_command("~/.local/bin/uv sync")

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
