from instant_python.configuration.question.question import Question
from instant_python.configuration.question.questionary import Questionary


class MultipleChoiceQuestion(Question[list[str]]):
    def __init__(self, key: str, message: str, options: list[str], questionary: Questionary) -> None:
        super().__init__(key, message, questionary)
        self._options = options

    def ask(self) -> dict[str, list[str]]:
        answer = self._questionary.multiselect_question(self._message, options=self._options)
        return {self._key: answer}
