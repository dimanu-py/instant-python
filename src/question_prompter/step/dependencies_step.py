from src.question_prompter.question.choice_question import ChoiceQuestion
from src.question_prompter.question.dependencies_question import DependenciesQuestion
from src.question_prompter.question.multiple_choice_question import MultipleChoiceQuestion
from src.question_prompter.step.steps import Step


class DependenciesStep(Step):
    def __init__(self) -> None:
        self._questions = [
            ChoiceQuestion(
                key="python_version",
                message="Enter the python version",
                default="3.13",
                options=["3.13", "3.12", "3.11", "3.10"],
            ),
            ChoiceQuestion(
                key="dependency_manager",
                message="Select a dependency manager",
                default="uv",
                options=["uv", "pdm"],
            ),
            ChoiceQuestion(
                key="shell",
                message="Select the shell you use",
                default="zsh",
                options=["zsh", "bash", "fish"],
            ),
            MultipleChoiceQuestion(
                key="built_in_features",
                message="Select the built-in features you want to include (fastapi_application option requires logger)",
                options=[
                    "value_objects",
                    "github_actions",
                    "makefile",
                    "synchronous_sqlalchemy",
                    "logger",
                    "event_bus",
                    "async_sqlalchemy",
                    "async_alembic",
                    "fastapi_application",
                ],
            ),
            DependenciesQuestion(
                key="dependencies",
                message="Do you want to install any dependencies?",
            )
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        for question in self._questions:
            answers_so_far[question.key] = question.ask()

        return answers_so_far

    def should_not_ask(self, answers_so_far: dict[str, str]) -> bool:
        return False
