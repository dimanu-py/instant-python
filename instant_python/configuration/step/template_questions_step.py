from instant_python.configuration.question.boolean_question import BooleanQuestion
from instant_python.configuration.question.choice_question import ChoiceQuestion
from instant_python.configuration.question.conditional_question import ConditionalQuestion
from instant_python.configuration.question.free_text_question import FreeTextQuestion
from instant_python.configuration.question.multiple_choice_question import MultipleChoiceQuestion
from instant_python.configuration.question.questionary import Questionary
from instant_python.configuration.step.steps import Step
from instant_python.configuration.template.template_types import TemplateTypes


class TemplateStep(Step):
    def __init__(self, questionary: Questionary) -> None:
        super().__init__(questionary)
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
                questionary=self._questionary,
            ),
            ConditionalQuestion(
                base_question=ChoiceQuestion(
                    key="template",
                    message="Select a template",
                    options=[
                        "domain_driven_design",
                        "clean_architecture",
                        "standard_project",
                        "custom",
                    ],
                    questionary=self._questionary,
                ),
                subquestions=ConditionalQuestion(
                    base_question=BooleanQuestion(
                        key="specify_bounded_context",
                        message="Do you want to specify your first bounded context?",
                        default=True,
                        questionary=self._questionary,
                    ),
                    subquestions=[
                        FreeTextQuestion(
                            key="bounded_context",
                            message="Enter the bounded context name",
                            default="backoffice",
                            questionary=self._questionary,
                        ),
                        FreeTextQuestion(
                            key="aggregate_name",
                            message="Enter the aggregate name",
                            default="user",
                            questionary=self._questionary,
                        ),
                    ],
                    condition=True,
                ),
                condition=TemplateTypes.DDD,
            ),
        ]

    def run(self) -> dict[str, dict[str, str | list[str]]]:
        answers = {}
        for question in self._questions:
            answers.update(question.ask())

        return {"template": answers}
