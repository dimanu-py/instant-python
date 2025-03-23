import questionary

from instant_python.question_prompter.question.question import Question


class MultipleChoiceQuestion(Question[list[str]]):
    def __init__(self, key: str, message: str, options: list[str]) -> None:
        super().__init__(key, message)
        self._options = options
    
    def ask(self) -> dict[str, list[str]]:
        answer = questionary.checkbox(self._message, choices=self._options).ask()
        return {self._key: answer}
