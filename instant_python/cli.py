import typer

from instant_python.installer.dependency_manager_factory import DependencyManagerFactory
from instant_python.installer.git_configurer import GitConfigurer
from instant_python.installer.installer import Installer
from instant_python.project_generator.folder_tree import FolderTree
from instant_python.project_generator.project_generator import ProjectGenerator
from instant_python.project_generator.template_manager import TemplateManager
from instant_python.question_prompter.question_wizard import QuestionWizard
from instant_python.question_prompter.step.dependencies_step import DependenciesStep
from instant_python.question_prompter.step.domain_driven_design_step import DomainDrivenDesignStep
from instant_python.question_prompter.step.general_project_step import GeneralProjectStep
from instant_python.question_prompter.step.git_step import GitStep
from instant_python.question_prompter.step.steps import Steps

app = typer.Typer()


@app.command()
def generate_project() -> None:
    wizard = QuestionWizard(
        steps=(
            Steps(
                GeneralProjectStep(),
                DomainDrivenDesignStep(),
                GitStep(),
                DependenciesStep(),
            )
        )
    )
    user_requirements = wizard.run()
    user_requirements.save_in_memory()

    project_generator = ProjectGenerator(
        folder_tree=FolderTree(user_requirements.project_slug), template_manager=TemplateManager()
    )
    project_generator.generate()

    installer = Installer(
        dependency_manager=DependencyManagerFactory.create(
            user_requirements.dependency_manager, project_generator.path
        )
    )
    installer.perform_installation(
        user_requirements.python_version, user_requirements.dependencies
    )

    if user_requirements.git:
        git_configurer = GitConfigurer(project_generator.path)
        git_configurer.configure(user_requirements.git_email, user_requirements.git_user_name)
    user_requirements.remove()


if __name__ == "__main__":
    app()
