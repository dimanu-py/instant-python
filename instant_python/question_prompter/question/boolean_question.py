import questionary

from instant_python.question_prompter.question.question import Question


class BooleanQuestion(Question[bool]):
    def __init__(self, key: str, message: str, default: bool) -> None:
        super().__init__(key, message)
        self._default = default

    def ask(self) -> dict[str, bool]:
        answer = questionary.confirm(self._message, default=self._default).ask()
        return {self._key: answer}
