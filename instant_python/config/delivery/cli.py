import typer

from instant_python.configuration.parser.parser import Parser
from instant_python.config.infra.question_wizard.question import Questionary
from instant_python.config.infra.question_wizard.questionary_console_wizard import QuestionaryConsoleWizard
from instant_python.config.infra.question_wizard.step import DependenciesStep
from instant_python.config.infra.question_wizard.step import GeneralStep
from instant_python.config.infra.question_wizard.step import GitStep
from instant_python.config.infra.question_wizard.step import Steps
from instant_python.config.infra.question_wizard.step import TemplateStep

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

    question_wizard = QuestionaryConsoleWizard(steps=steps)
    configuration = question_wizard.run()
    validated_configuration = Parser.parse_from_answers(configuration)
    validated_configuration.save_on_current_directory()
