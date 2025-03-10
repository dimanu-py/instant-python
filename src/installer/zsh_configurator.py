import subprocess
from typing import override

from src.installer.shell_configurator import ShellConfigurator


class ZshConfigurator(ShellConfigurator):
    def __init__(self) -> None:
        self._executable = "/bin/zsh"

    @override
    def configure_shell_completion(self) -> None:
        print(">>> Configuring zsh...")
        subprocess.run(
            r'echo \'eval "$(uv generate-shell-completion zsh)"\' >> ~/.zshrc',
            shell=True,
            check=True,
            executable=self._executable,
        )
        subprocess.run(
            r'echo \'eval "$(uvx --generate-shell-completion zsh)"\' >> ~/.zshrc',
            shell=True,
            check=True,
            executable=self._executable,
        )
        print(">>> zsh configured successfully")
