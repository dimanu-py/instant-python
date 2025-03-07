import subprocess

from src.installer.dependency_manager import DependencyManager


class UvManager(DependencyManager):
    def __init__(self) -> None:
        self._uv_command = "curl -LsSf https://astral.sh/uv/install.sh | sh"
        self._python_command = "~/.local/bin/uv python install"
        self._executable = "/bin/bash"

    def install(self) -> None:
        print(">>> Installing uv...")
        subprocess.run(self._uv_command, shell=True, check=True, executable=self._executable)
        print(">>> uv installed successfully")

    def install_python(self, version: str) -> None:
        command = f"{self._python_command} {version}"
        print(f">>> Installing Python {version}...")
        subprocess.run(command, shell=True, check=True, executable=self._executable)
        print(f">>> Python {version} installed successfully")
