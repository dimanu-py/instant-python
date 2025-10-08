import typer

from instant_python.config.application.config_generator import ConfigGenerator
from instant_python.config.infra.parser.parser import Parser
from instant_python.config.infra.question_wizard.step.questionary import Questionary
from instant_python.config.infra.question_wizard.questionary_console_wizard import QuestionaryConsoleWizard
from instant_python.config.infra.question_wizard.step.dependencies_step import DependenciesStep
from instant_python.config.infra.question_wizard.step.general_step import GeneralStep
from instant_python.config.infra.question_wizard.step.git_step import GitStep
from instant_python.config.infra.question_wizard.step.steps import Steps
from instant_python.config.infra.question_wizard.step.template_step import TemplateStep
from instant_python.config.infra.writer.yaml_config_writer import YamlConfigWriter

app = typer.Typer()


@app.command("config", help="Generate the configuration file for a new project")
def generate_ipy_configuration_file() -> None:
    questionary = Questionary()
    question_wizard = QuestionaryConsoleWizard(
        steps=(
            Steps(
                GeneralStep(questionary=questionary),
                TemplateStep(questionary=questionary),
                GitStep(questionary=questionary),
                DependenciesStep(questionary=questionary),
            )
        )
    )

    config_generator = ConfigGenerator(
        question_wizard=question_wizard,
        writer=YamlConfigWriter(),
        parser=Parser(),
    )
    config_generator.execute()
