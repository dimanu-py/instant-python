from instant_python.question_prompter.question.choice_question import ChoiceQuestion
from instant_python.question_prompter.question.free_text_question import (
    FreeTextQuestion,
)
from instant_python.question_prompter.question.multiple_choice_question import (
    MultipleChoiceQuestion,
)
from instant_python.question_prompter.step.steps import Step


class TemplateStep(Step):
    def __init__(self) -> None:
        self._questions = [
            ChoiceQuestion(
                key="template",
                message="Select a template",
                options=[
                    "domain_driven_design",
                    "clean_architecture",
                    "standard_project",
                ],
            ),
            FreeTextQuestion(
                key="bounded_context",
                message="Enter the bounded context name",
                default="backoffice",
            ),
            FreeTextQuestion(
                key="aggregate_name", message="Enter the aggregate name", default="user"
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
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        template = self._questions[0].ask()
        answers_so_far[self._questions[0].key] = template
        if template == "domain_driven_design":
            for question in self._questions[1:3]:
                answers_so_far[question.key] = question.ask()
        else:
            for question in self._questions[3:]:
                answers_so_far[question.key] = question.ask()
            
        return answers_so_far
