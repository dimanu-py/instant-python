import subprocess
from typing import override

from src.installer.shell_configurator import ShellConfigurator


class BashConfigurator(ShellConfigurator):
    def __init__(self) -> None:
        self._executable = "/bin/bash"

    @override
    def configure_shell_completion(self) -> None:
        print(">>> Configuring bash...")
        subprocess.run(
            r'echo \'eval "$(uv generate-shell-completion bash)"\' >> ~/.bashrc',
            shell=True,
            check=True,
            executable=self._executable,
        )
        subprocess.run(
            r'echo \'eval "$(uvx --generate-shell-completion bash)"\' >> ~/.bashrc',
            shell=True,
            check=True,
            executable=self._executable,
        )
        print(">>> bash configured successfully")
