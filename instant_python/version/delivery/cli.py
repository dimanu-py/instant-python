import typer
from rich.console import Console

from instant_python import __version__
from instant_python.version.infra.py_pi_version_repository import PyPiLatestLatestVersionRepository
from instant_python.version.infra.urllib_http_client import UrllibHttpClient

app = typer.Typer()
console = Console()


@app.command("version", help="Show instant-python version")
def show_version() -> None:
    latest_version_repository = PyPiLatestLatestVersionRepository(client=UrllibHttpClient())
    latest_version = latest_version_repository.get_latest_version()
    current_version = __version__
    console.print(f"{current_version} - (latest) {latest_version}")
