from src.installer.bash_configurator import BashConfigurator
from src.installer.fish_configurator import FishConfigurator
from src.installer.shell_configurator import ShellConfigurator
from src.installer.shells import Shells
from src.installer.zsh_configurator import ZshConfigurator


class ShellConfiguratorFactory:
    @staticmethod
    def create(user_shell: str) -> ShellConfigurator:
        shells = {
            Shells.ZSH: ZshConfigurator,
            Shells.BASH: BashConfigurator,
            Shells.FISH: FishConfigurator,
        }

        return shells[Shells(user_shell)]()
