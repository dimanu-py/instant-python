import typer
from instant_python import folder_cli, project_cli
from instant_python.errors.application_error import ApplicationError
from instant_python.intant_python_typer import InstantPythonTyper

app = InstantPythonTyper()

app.add_typer(folder_cli.app, name="folder", help="Generate only the folder structure for a new project")
app.add_typer(project_cli.app, name="project", help="Generate a full project ready to be used")


@app.error_handler(ApplicationError)
def handle_application_error(exc: ApplicationError) -> None:
    typer.secho(f"Error: {exc.message}", err=True, fg=typer.colors.RED)
    typer.Exit(code=-1)


@app.error_handler(Exception)
def handle_unexpected_error(exc: Exception) -> None:
    typer.secho(f"An unexpected error occurred: {exc}", err=True, fg=typer.colors.RED)
    typer.Exit(code=-1)


if __name__ == "__main__":
    app()
