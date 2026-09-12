import os
import platform
import shutil

from instant_python.shared.application_error import ApplicationError
from instant_python.shared.infra.system_console import SystemConsole
from instant_python.version.domain.updater import LATEST_VERSION, Updater

_REPO = "dimanu-py/instant-python"
_INSTALL_SCRIPT_SH_URL = f"https://raw.githubusercontent.com/{_REPO}/main/scripts/install.sh"
_INSTALL_SCRIPT_PS1_URL = f"https://raw.githubusercontent.com/{_REPO}/main/scripts/install.ps1"


class BinaryUpdater(Updater):
    def __init__(self, console: SystemConsole) -> None:
        self._console = console

    def update(self, version: str) -> None:
        if version == LATEST_VERSION:
            self._update_to_latest()
        else:
            self._reinstall_pinned_version(version)

    def _update_to_latest(self) -> None:
        binary_path = self._locate_binary()
        self._console.execute_or_raise(f'"{binary_path}" self update')

    def _reinstall_pinned_version(self, version: str) -> None:
        command = self._pinned_install_command(version)
        self._console.execute_or_raise(command)

    @staticmethod
    def _pinned_install_command(version: str) -> str:
        if platform.system() == "Windows":
            return f"powershell -ExecutionPolicy ByPass -c \"$env:IPY_VERSION='{version}'; irm {_INSTALL_SCRIPT_PS1_URL} | iex\""
        return f"curl -LsSf {_INSTALL_SCRIPT_SH_URL} | IPY_VERSION={version} sh"

    @staticmethod
    def _locate_binary() -> str:
        pyapp_location = os.environ.get("PYAPP")
        if pyapp_location and pyapp_location != "1":
            return pyapp_location

        binary_path = shutil.which("ipy")
        if binary_path is None:
            raise IpyBinaryNotFoundError()
        return binary_path


class IpyBinaryNotFoundError(ApplicationError):
    def __init__(self) -> None:
        super().__init__(message="Could not locate the 'ipy' binary on your PATH to update it")
