import typer

from instant_python.configuration.parser.parser import Parser
from instant_python.configuration.question.questionary import Questionary
from instant_python.configuration.question_wizard import QuestionWizard
from instant_python.configuration.step.dependencies_step import DependenciesStep
from instant_python.configuration.step.general_step import GeneralStep
from instant_python.configuration.step.git_step import GitStep
from instant_python.configuration.step.steps import Steps
from instant_python.configuration.step.template_step import TemplateStep

app = typer.Typer()


@app.command("config", help="Generate the configuration file for a new project")
def create_new_project() -> None:
    questionary = Questionary()
    steps = Steps(
        GeneralStep(questionary=questionary),
        TemplateStep(questionary=questionary),
        GitStep(questionary=questionary),
        DependenciesStep(questionary=questionary),
    )

    question_wizard = QuestionWizard(steps=steps)
    configuration = question_wizard.run()
    validated_configuration = Parser.parse_from_answers(configuration)
    validated_configuration.save_on_current_directory()
