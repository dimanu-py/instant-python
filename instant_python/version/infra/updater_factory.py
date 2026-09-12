from collections.abc import Callable

from instant_python.shared.infra.system_console import SystemConsole
from instant_python.version.domain.installation_method import InstallationMethod
from instant_python.version.domain.updater import Updater
from instant_python.version.domain.updater_resolver import UpdaterResolver
from instant_python.version.infra.binary_updater import BinaryUpdater
from instant_python.version.infra.pip_updater import PipUpdater
from instant_python.version.infra.pipx_updater import PipxUpdater
from instant_python.version.infra.uv_updater import UvUpdater


class UpdaterFactory(UpdaterResolver):
    def __init__(self, console: SystemConsole) -> None:
        self._console = console

    def resolve(self, installation_method: InstallationMethod) -> Updater:
        updaters: dict[InstallationMethod, Callable[[SystemConsole], Updater]] = {
            InstallationMethod.BINARY: BinaryUpdater,
            InstallationMethod.PIPX: PipxUpdater,
            InstallationMethod.UV: UvUpdater,
            InstallationMethod.PIP: PipUpdater,
        }
        return updaters[installation_method](self._console)
