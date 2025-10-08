from instant_python.config.infra.question_wizard.question.question import Question
from instant_python.config.infra.question_wizard.question.questionary import Questionary


class BooleanQuestion(Question[bool]):
    def __init__(self, key: str, message: str, default: bool, questionary: Questionary) -> None:
        super().__init__(key, message, questionary)
        self._default = default

    def ask(self) -> dict[str, bool]:
        answer = self._questionary.boolean_question(self._message, default=self._default)
        return {self._key: answer}
