import subprocess
from typing import override

from src.installer.shell_configurator import ShellConfigurator


class FishConfigurator(ShellConfigurator):
    def __init__(self) -> None:
        self._executable = "/usr/bin/fish"

    @override
    def configure_shell_completion(self) -> None:
        print(">>> Configuring fish...")
        subprocess.run(
            r'echo \'uv generate-shell-completion fish | source\' >> ~/.config/fish/config.fish',
            shell=True,
            check=True,
            executable=self._executable,
        )
        subprocess.run(
            r'echo \'uvx --generate-shell-completion fish | source\' >> ~/.config/fish/config.fish',
            shell=True,
            check=True,
            executable=self._executable,
        )
        print(">>> fish configured successfully")
