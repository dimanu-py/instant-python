import questionary

from src.question_prompter.question import Question
from src.question_prompter.questions_definition import (
    GENERAL_QUESTIONS,
    DDD_QUESTIONS,
)
from src.question_prompter.template_types import TemplateTypes
from src.question_prompter.user_requirements import UserRequirements


class BasicPrompter:
    def __init__(self) -> None:
        self._answers = {}

    def ask(self) -> UserRequirements:
        self._answers = {
            question.key: question.ask()
            for question in GENERAL_QUESTIONS
        }

        if self._is_ddd_template():
            ddd_answers = {
                question.key: question.ask()
                for question in DDD_QUESTIONS
            }
            self._answers.update(ddd_answers)

        return UserRequirements(**self._answers)

    def _is_ddd_template(self) -> bool:
        return self._answers["template"] == TemplateTypes.DDD
