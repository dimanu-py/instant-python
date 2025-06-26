from typing import Optional

from instant_python.configuration.question.question import Question
from instant_python.configuration.question.questionary import Questionary


class FreeTextQuestion(Question[str]):
    def __init__(self, key: str, message: str, questionary: Questionary, default: Optional[str] = None) -> None:
        super().__init__(key, message, questionary)
        self._default = default if default else ""

    def ask(self) -> dict[str, str]:
        answer = self._questionary.free_text_question(self._message, default=self._default)
        return {self._key: answer}
