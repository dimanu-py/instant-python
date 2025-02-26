from typing import Any

import questionary

from instant_python.question_prompter.question import Question
from instant_python.question_prompter.questions_definition import (
    GENERAL_QUESTIONS,
    DDD_QUESTIONS,
)
from instant_python.question_prompter.template_types import TemplateTypes
from instant_python.question_prompter.user_requirements import UserRequirements


class BasicPrompter:
    def ask(self) -> UserRequirements:
        answers = {
            question.key: self._ask_single_question(question)
            for question in GENERAL_QUESTIONS
        }

        if answers["template"] == TemplateTypes.DDD:
            ddd_answers = {
                question.key: self._ask_single_question(question)
                for question in DDD_QUESTIONS
            }
            answers.update(ddd_answers)

        return UserRequirements(**answers)

    def _ask_single_question(self, question: Question) -> str | bool:
        if question.confirm:
            return self._confirm(question.message)
        elif question.multiselect:
            return self._multiselect(question.message, question.options)
        return self._prompt(question.message, question.default, question.options)

    @staticmethod
    def _prompt(
        text: str,
        default_value: str,
        options: list[str],
    ) -> str:
        if not options:
            return questionary.text(text, default=default_value).ask()
        return questionary.select(
            text,
            choices=options,
            default=default_value,
        ).ask()

    @staticmethod
    def _confirm(text: str) -> bool:
        return questionary.confirm(text, default=True).ask()

    @staticmethod
    def _multiselect(message: str, options: list[str]) -> str:
        return questionary.checkbox(message, choices=options).ask()
