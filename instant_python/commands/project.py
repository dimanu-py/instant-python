import typer

from instant_python.configuration.parser.parser import Parser

app = typer.Typer()


@app.command("new", help="Create a new project")
def create_new_project(config_file: str = typer.Option(..., "--config", "-c", help="Path to yml configuration file")):
    configuration = Parser.parse(config_file_path=config_file)
