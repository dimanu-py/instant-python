import subprocess
from typing import override

from src.installer.shell_configurator import ShellConfigurator


class ZshConfigurator(ShellConfigurator):
    def __init__(self) -> None:
        self._executable = "/bin/bash"
        self._command = r"export PATH=\"$HOME/.local/bin:$PATH\""

    @override
    def configure_shell_completion(self) -> None:
        print(">>> Configuring zsh...")
        subprocess.run(
            self._command, shell=True, check=True, executable=self._executable
        )
        print(">>> zsh configured successfully")
