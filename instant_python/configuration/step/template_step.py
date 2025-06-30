from typing import Union

from instant_python.configuration.question.boolean_question import BooleanQuestion
from instant_python.configuration.question.choice_question import ChoiceQuestion
from instant_python.configuration.question.conditional_question import ConditionalQuestion
from instant_python.configuration.question.free_text_question import FreeTextQuestion
from instant_python.configuration.question.multiple_choice_question import MultipleChoiceQuestion
from instant_python.configuration.question.questionary import Questionary
from instant_python.configuration.step.steps import Step
from instant_python.shared.supported_built_in_features import SupportedBuiltInFeatures
from instant_python.shared.supported_templates import SupportedTemplates


class TemplateStep(Step):
    def __init__(self, questionary: Questionary) -> None:
        super().__init__(questionary)
        self._built_in_features_question = MultipleChoiceQuestion(
            key="built_in_features",
            message="Select the built-in features you want to include",
            options=SupportedBuiltInFeatures.get_supported_built_in_features(),
            questionary=self._questionary,
        )
        self._template_question = ConditionalQuestion(
            base_question=ChoiceQuestion(
                key="name",
                message="Select a template",
                options=SupportedTemplates.get_supported_templates(),
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
            condition=SupportedTemplates.DDD,
        )

    def run(self) -> dict[str, dict[str, Union[str, list[str]]]]:
        answers = self._template_question.ask()

        if answers["name"] != SupportedTemplates.CUSTOM:
            answers.update(self._built_in_features_question.ask())

        return {"template": answers}
