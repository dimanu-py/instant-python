from pathlib import Path

import typer
from rich.console import Console

from instant_python import __version__
from instant_python.shared.infra.system_console import SystemConsole
from instant_python.version.application.version_updater import VersionUpdater
from instant_python.version.domain.updater import LATEST_VERSION
from instant_python.version.infra.py_pi_version_repository import PyPiLatestLatestVersionRepository
from instant_python.version.infra.system_installation_method_detector import SystemInstallationMethodDetector
from instant_python.version.infra.updater_factory import UpdaterFactory
from instant_python.version.infra.urllib_http_client import UrllibHttpClient

app = typer.Typer()
console = Console()


@app.command("version", help="Show instant-python version")
def show_version() -> None:
    latest_version_repository = PyPiLatestLatestVersionRepository(client=UrllibHttpClient())
    latest_version = latest_version_repository.get_latest_version()
    current_version = __version__
    console.print(f"{current_version} - (latest) {latest_version}")


@app.command("update", help="Update instant-python to the latest version or a specific one")
def update_version(
    version: str = typer.Option(LATEST_VERSION, "--version", help="Specific version to install instead of the latest"),
) -> None:
    version_updater = VersionUpdater(
        detector=SystemInstallationMethodDetector(),
        updater_resolver=UpdaterFactory(console=SystemConsole(working_directory=str(Path.cwd()))),
    )

    console.print(f"Updating instant-python to {version}...")
    installation_method = version_updater.execute(version)
    console.print(f"instant-python updated successfully (installed via {installation_method.value})")
