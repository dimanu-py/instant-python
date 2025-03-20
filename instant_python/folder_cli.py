import typer

from instant_python.project_generator.custom_template_manager import CustomTemplateManager
from instant_python.project_generator.default_template_manager import DefaultTemplateManager
from instant_python.project_generator.folder_tree import FolderTree
from instant_python.project_generator.project_generator import ProjectGenerator
from instant_python.question_prompter.question.free_text_question import FreeTextQuestion
from instant_python.question_prompter.question_wizard import QuestionWizard
from instant_python.question_prompter.step.domain_driven_design_step import DomainDrivenDesignStep
from instant_python.question_prompter.step.general_project_step import GeneralProjectStep
from instant_python.question_prompter.step.steps import Steps

app = typer.Typer()


@app.command("template", help="Create all the folders and files for a new project using a custom template")
def template(template_name: str) -> None:
	project_name = FreeTextQuestion(
		key="project_slug",
		message="Enter the name of the project (CANNOT CONTAIN SPACES)",
		default="python-project",
	).ask()
	project_generator = ProjectGenerator(
		folder_tree=FolderTree(project_name),
		template_manager=CustomTemplateManager(template_name),
	)

	project_generator.generate()


@app.command("new", help="Create all the folders and files for a new project")
def new() -> None:
	wizard = QuestionWizard(
		steps=Steps(GeneralProjectStep(), DomainDrivenDesignStep())
	)
	user_requirements = wizard.run()
	user_requirements.save_in_memory()

	project_generator = ProjectGenerator(
		folder_tree=FolderTree(user_requirements.project_slug),
		template_manager=DefaultTemplateManager(),
	)

	project_generator.generate()

	user_requirements.remove()


if __name__ == "__main__":
	app()