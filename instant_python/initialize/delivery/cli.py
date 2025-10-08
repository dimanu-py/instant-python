import typer

from instant_python.configuration.parser.parser import Parser
from instant_python.dependency_manager.dependency_manager_factory import DependencyManagerFactory
from instant_python.formatter.project_formatter import ProjectFormatter
from instant_python.git.git_configurer import GitConfigurer
from instant_python.project_creator.file_system import FileSystem
from instant_python.render.custom_project_renderer import CustomProjectRenderer
from instant_python.render.jinja_environment import JinjaEnvironment
from instant_python.render.jinja_project_renderer import JinjaProjectRenderer

app = typer.Typer()


@app.command("init", help="Create a new project")
def create_new_project(
    config_file: str = typer.Option("ipy.yml", "--config", "-c", help="Path to yml configuration file"),
    template: str | None = typer.Option(None, "--template", "-t", help="Path to custom template file"),
) -> None:
    configuration = Parser.parse_from_file(config_file_path=config_file)
    environment = JinjaEnvironment(package_name="instant_python", template_directory="templates")

    if template:
        project_renderer = CustomProjectRenderer(template_path=template)
        project_structure = project_renderer.render_project_structure()
    else:
        project_renderer = JinjaProjectRenderer(jinja_environment=environment)
        project_structure = project_renderer.render_project_structure(
            context_config=configuration,
            template_base_dir="project_structure",
        )

    file_system = FileSystem(project_structure=project_structure)
    file_system.write_on_disk(
        file_renderer=environment,
        context=configuration,
    )

    dependency_manager = DependencyManagerFactory.create(
        dependency_manager=configuration.dependency_manager,
        project_directory=configuration.project_folder_name,
    )
    dependency_manager.setup_environment(
        python_version=configuration.python_version,
        dependencies=configuration.dependencies,
    )

    formatter = ProjectFormatter(project_directory=configuration.project_folder_name)
    formatter.format()

    configuration.save_on_project_folder()
    git_configurer = GitConfigurer(project_directory=configuration.project_folder_name)
    git_configurer.setup_repository(configuration.git)


if __name__ == "__main__":
    app()
