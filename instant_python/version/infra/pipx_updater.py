from instant_python.shared.infra.system_console import SystemConsole
from instant_python.version.domain.updater import LATEST_VERSION, Updater


class PipxUpdater(Updater):
    _PACKAGE_NAME = "instant-python"

    def __init__(self, console: SystemConsole) -> None:
        self._console = console

    def update(self, version: str) -> None:
        command = (
            f"pipx upgrade {self._PACKAGE_NAME}"
            if version == LATEST_VERSION
            else f"pipx install {self._PACKAGE_NAME}=={version} --force"
        )
        self._console.execute_or_raise(command)
