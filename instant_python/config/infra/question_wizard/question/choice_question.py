from typing import Optional

from instant_python.config.infra.question_wizard.question.question import Question
from instant_python.config.infra.question_wizard.question.questionary import Questionary


class ChoiceQuestion(Question[str]):
    def __init__(self, key: str, message: str, questionary: Questionary, options: Optional[list[str]] = None) -> None:
        super().__init__(key, message, questionary)
        self._default = options[0] if options else ""
        self._options = options if options else []

    def ask(self) -> dict[str, str]:
        answer = self._questionary.single_choice_question(
            self._message,
            options=self._options,
            default=self._default,
        )
        return {self._key: answer}
