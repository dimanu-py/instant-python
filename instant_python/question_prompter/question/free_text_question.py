import questionary

from instant_python.question_prompter.question.question import Question


class FreeTextQuestion(Question[str]):
    def __init__(self, key: str, message: str, default: str | None = None) -> None:
        super().__init__(key, message)
        self._default = default if default else ""
    
    def ask(self) -> dict[str, str]:
        answer = questionary.text(self._message, default=self._default).ask()
        return {self._key: answer}
