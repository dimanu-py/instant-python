import subprocess


class UvDependencyManager:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

    def _install(self) -> None:
        print(">>> Installing uv...")
        self._run_command(command="curl -LsSf https://astral.sh/uv/install.sh | sh")
        print(">>> uv installed successfully")

    def _install_python(self, version: str) -> None:
        print(f">>> Installing Python {version}...")
        self._run_command(command=f"~/.local/bin/uv python install {version}")
        print(f">>> Python {version} installed successfully")

    def _install_dependencies(self, dependencies: list[dict]) -> None:
        self._run_command("~/.local/bin/uv sync")
        for dependency in dependencies:
            name = dependency["name"]
            version = dependency["version"]
            is_dev = dependency.get("is_dev", False)
            group = dependency.get("group", None)

            flag = "--dev" if is_dev else None
            if group:
                flag = f"{flag} --group {group}"

            dependency_name = f"{name}=={version}" if version != "latest" else name
            command = f"~/.local/bin/uv add {flag} {dependency_name}" if flag else f"~/.local/bin/uv add {dependency_name}"
            self._run_command(command)

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
