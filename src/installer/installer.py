from src.installer.dependency_manager import DependencyManager
from src.installer.shell_configurator import ShellConfigurator


class Installer:
    _dependency_manager: DependencyManager
    _shell_configurator: ShellConfigurator

    def __init__(
        self,
        dependency_manager: DependencyManager,
        shell_configurator: ShellConfigurator,
    ) -> None:
        self._shell_configurator = shell_configurator
        self._dependency_manager = dependency_manager

    def perform_installation(self, python_version: str) -> None:
        self._dependency_manager.install()
        self._shell_configurator.configure()
        self._dependency_manager.install_python(python_version)
