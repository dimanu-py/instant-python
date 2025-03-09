from pathlib import Path

import typer

from src.installer.installer import Installer
from src.installer.uv_manager import UvManager
from src.installer.zsh_configurator import ZshConfigurator
from src.project_generator.folder_tree import FolderTree
from src.project_generator.project_generator import ProjectGenerator
from src.project_generator.template_manager import TemplateManager
from src.question_prompter.question_wizard import QuestionWizard
from src.question_prompter.step.dependencies_step import DependenciesStep
from src.question_prompter.step.domain_driven_design_step import DomainDrivenDesignStep
from src.question_prompter.step.general_project_step import GeneralProjectStep
from src.question_prompter.step.steps import Steps
from src.question_prompter.user_requirements import UserRequirements

app = typer.Typer()


def user_requirements_has_not_been_generated_before() -> bool:
    return Path("user_requirements.yml").exists() is False


@app.command()
def generate_project():
    if user_requirements_has_not_been_generated_before():
        wizard = QuestionWizard(
            steps=(
                Steps(
                    GeneralProjectStep(), DomainDrivenDesignStep(), DependenciesStep()
                )
            )
        )
        user_requirements = wizard.run()
        user_requirements.save_in_memory()
    else:
        user_requirements = UserRequirements.load_from_file()

    project_generator = ProjectGenerator(
        folder_tree=FolderTree(), template_manager=TemplateManager()
    )
    project_generator.generate()

    installer = Installer(
        dependency_manager=UvManager(), shell_configurator=ZshConfigurator()
    )
    installer.perform_installation(
        user_requirements.python_version, user_requirements.dependencies
    )


if __name__ == "__main__":
    app()
