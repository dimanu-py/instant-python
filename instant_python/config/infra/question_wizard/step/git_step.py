from typing import Union

from instant_python.config.infra.question_wizard.question.boolean_question import BooleanQuestion
from instant_python.config.infra.question_wizard.question.conditional_question import ConditionalQuestion
from instant_python.config.infra.question_wizard.question.free_text_question import FreeTextQuestion
from instant_python.config.infra.question_wizard.question.questionary import Questionary
from instant_python.config.infra.question_wizard.step.steps import Step


class GitStep(Step):
    def __init__(self, questionary: Questionary) -> None:
        super().__init__(questionary)
        self._questions = [
            ConditionalQuestion(
                base_question=BooleanQuestion(
                    key="initialize",
                    message="Do you want to initialize a git repository?",
                    default=True,
                    questionary=self._questionary,
                ),
                subquestions=[
                    FreeTextQuestion(
                        key="username",
                        message="Type your git user name",
                        questionary=self._questionary,
                    ),
                    FreeTextQuestion(
                        key="email",
                        message="Type your git email",
                        questionary=self._questionary,
                    ),
                ],
                condition=True,
            )
        ]

    def run(self) -> dict[str, dict[str, Union[str, bool]]]:
        answers = {}
        for question in self._questions:
            answers.update(question.ask())
        return {"git": answers}
