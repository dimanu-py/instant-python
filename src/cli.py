from pathlib import Path

import typer

from src.installer.installer import Installer
from src.installer.uv_manager import UvManager
from src.installer.zsh_configurator import ZshConfigurator
from src.project_generator.project_generator import ProjectGenerator
from src.question_prompter.basic_prompter import BasicPrompter
from src.question_prompter.user_requirements import UserRequirements

app = typer.Typer()


def user_requirements_has_not_been_generated_before() -> bool:
    return Path("user_requirements.yml").exists() is False


@app.command()
def generate_project():
    if user_requirements_has_not_been_generated_before():
        user_requirements = BasicPrompter().ask()
        user_requirements.save_in_memory()
    else:
        user_requirements = UserRequirements.load_from_file()

    project_generator = ProjectGenerator()
    project_generator.generate()

    installer = Installer(
        dependency_manager=UvManager(),
        shell_configurator=ZshConfigurator()
    )
    installer.perform_installation(user_requirements.python_version)


if __name__ == "__main__":
    app()
