import typer

from instant_python import folder_cli, project_cli

app = typer.Typer()
app.add_typer(folder_cli.app, name="folder")
app.add_typer(project_cli.app, name="project")


if __name__ == "__main__":
    app()
