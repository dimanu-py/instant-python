from rich.console import Console
from rich.panel import Panel

from instant_python.commands import folder_cli, project_cli, project
from instant_python.errors.application_error import ApplicationError
from instant_python.instant_python_typer import InstantPythonTyper

app = InstantPythonTyper()
console = Console()

app.add_typer(
    folder_cli.app,
    name="folder",
    help="Generate only the folder structure for a new project",
)
app.add_typer(project_cli.app, name="project", help="Generate a full project ready to be used")
app.add_typer(project.app)


@app.error_handler(ApplicationError)
def handle_application_error(exc: ApplicationError) -> None:
    error_panel = Panel(exc.message, title="Error", border_style="red")
    console.print(error_panel)


@app.error_handler(Exception)
def handle_unexpected_error(exc: Exception) -> None:
    error_panel = Panel(f"An unexpected error occurred: {exc}", title="Error", border_style="red")
    console.print(error_panel)


if __name__ == "__main__":
    app()
