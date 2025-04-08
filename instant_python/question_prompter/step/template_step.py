from instant_python.question_prompter.question.boolean_question import BooleanQuestion
from instant_python.question_prompter.question.choice_question import ChoiceQuestion
from instant_python.question_prompter.question.conditional_question import (
    ConditionalQuestion,
)
from instant_python.question_prompter.question.free_text_question import (
    FreeTextQuestion,
)
from instant_python.question_prompter.question.multiple_choice_question import (
    MultipleChoiceQuestion,
)
from instant_python.question_prompter.step.steps import Step
from instant_python.question_prompter.template_types import TemplateTypes


class TemplateStep(Step):
    def __init__(self) -> None:
        self._questions = [
            MultipleChoiceQuestion(
                key="built_in_features",
                message="Select the built-in features you want to include",
                options=[
                    "value_objects",
                    "github_actions",
                    "makefile",
                    "logger",
                    "event_bus",
                    "async_sqlalchemy",
                    "async_alembic",
                    "fastapi_application",
                ],
            ),
            ConditionalQuestion(
                base_question=ChoiceQuestion(
                    key="template",
                    message="Select a template",
                    options=[
                        "domain_driven_design",
                        "clean_architecture",
                        "standard_project",
                    ],
                ),
                subquestions=ConditionalQuestion(
                    base_question=BooleanQuestion(
                        key="specify_bounded_context",
                        message="Do you want to specify your first bounded context?",
                        default=True,
                    ),
                    subquestions=[
                        FreeTextQuestion(
                            key="bounded_context",
                            message="Enter the bounded context name",
                            default="backoffice",
                        ),
                        FreeTextQuestion(
                            key="aggregate_name",
                            message="Enter the aggregate name",
                            default="user",
                        ),
                    ],
                    condition=True,
                ),
                condition=TemplateTypes.DDD,
            ),
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        for question in self._questions:
            answers_so_far.update(question.ask())

        return answers_so_far
