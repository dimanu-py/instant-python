import typer
from click import Choice

from instant_python.question_prompter.question import Question
from instant_python.question_prompter.questions_definition import (
    GENERAL_QUESTIONS,
    DDD_QUESTIONS,
)
from instant_python.question_prompter.user_requirements import UserRequirements


class BasicPrompter:
    def ask(self) -> UserRequirements:
        answers = {
            question.key: self._ask_single_question(question)
            for question in GENERAL_QUESTIONS
        }

        if answers["template"] == "Domain Driven Design":
            ddd_answers = {
                question.key: self._ask_single_question(question)
                for question in DDD_QUESTIONS
            }
            answers.update(ddd_answers)

        return UserRequirements(**answers)

    def _ask_single_question(self, question: Question) -> str | bool:
        if question.confirm:
            return self._confirm(question.message)
        return self._prompt(question.message, question.default, question.options)

    @staticmethod
    def _prompt(
        text: str,
        default_value: str | None = None,
        options: list[str] | None = None,
    ) -> str:
        options = Choice(options, case_sensitive=False) if options else None
        show_choices = True if options else False
        return typer.prompt(
            text=text,
            default=default_value,
            type=options,
            show_choices=show_choices,
        )

    @staticmethod
    def _confirm(text: str) -> bool:
        return typer.confirm(text, default=True)
