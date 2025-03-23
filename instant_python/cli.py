import typer

from instant_python import folder_cli, project_cli

app = typer.Typer()
app.add_typer(folder_cli.app, name="folder", help="Generate only the folder structure for a new project")
app.add_typer(project_cli.app, name="project", help="Generate a full project ready to be used")


if __name__ == "__main__":
    app()
