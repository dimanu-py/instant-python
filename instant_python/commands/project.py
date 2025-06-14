import typer

from instant_python.configuration.parser.parser import Parser
from instant_python.project_creator.file_system import FileSystem
from instant_python.render.jinja_environment import JinjaEnvironment

app = typer.Typer()


@app.command("new", help="Create a new project")
def create_new_project(config_file: str = typer.Option(..., "--config", "-c", help="Path to yml configuration file")) -> None:
    configuration = Parser.parse(config_file_path=config_file)
    environment = JinjaEnvironment(package_name="instant_python", template_directory="templates")
    project_structure = JinjaProjectRender(jinja_environment=environment)
    project_structure.render_project_structure(context_config=configuration, template_base_dir="project_structure")

    file_system = FileSystem(jinja_environment=environment)
    file_system.create_folders_and_files(context_config=configuration, template_base_dir="project_structure")
