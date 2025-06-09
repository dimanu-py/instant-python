import typer

from instant_python.render.jinja_environment import JinjaEnvironment
from instant_python.render.jinja_project_render import JinjaProjectRender
from instant_python.configuration.parser.parser import Parser

app = typer.Typer()


@app.command("new", help="Create a new project")
def create_new_project(config_file: str = typer.Option(..., "--config", "-c", help="Path to yml configuration file")):
    configuration = Parser.parse(config_file_path=config_file)
    
    environment = JinjaEnvironment(package_name="instant_python", template_directory="templates")
    project_structure = JinjaProjectRender(jinja_environment=environment)
    project_structure.render_project_structure(context_config=configuration, template_base_dir="project_structure")

