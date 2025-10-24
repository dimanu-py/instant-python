import typer

from instant_python.config.infra.parser.parser import Parser
from instant_python.dependency_manager.dependency_manager_factory import DependencyManagerFactory
from instant_python.formatter.project_formatter import ProjectFormatter
from instant_python.git.git_configurer import GitConfigurer
from instant_python.initialize.application.config_reader import ConfigReader
from instant_python.initialize.infra.configuration_repository import YamlConfigurationRepository
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
    config_reader = ConfigReader(
        repository=YamlConfigurationRepository(),
        parser=Parser(),
    )
    config = config_reader.execute(config_file_path=config_file)
    environment = JinjaEnvironment(package_name="instant_python", template_directory="templates")

    if template:
        project_renderer = CustomProjectRenderer(template_path=template)
        project_structure = project_renderer.render_project_structure()
    else:
        project_renderer = JinjaProjectRenderer(jinja_environment=environment)
        project_structure = project_renderer.render_project_structure(
            context_config=config,
            template_base_dir="project_structure",
        )

    file_system = FileSystem(project_structure=project_structure)
    file_system.write_on_disk(
        file_renderer=environment,
        context=config,
    )

    dependency_manager = DependencyManagerFactory.create(
        dependency_manager=config.dependency_manager,
        project_directory=config.project_folder_name,
    )
    dependency_manager.setup_environment(
        python_version=config.python_version,
        dependencies=config.dependencies,
    )

    formatter = ProjectFormatter(project_directory=config.project_folder_name)
    formatter.format()

    config.save_on_project_folder()
    git_configurer = GitConfigurer(project_directory=config.project_folder_name)
    git_configurer.setup_repository(config.git)


if __name__ == "__main__":
    app()
