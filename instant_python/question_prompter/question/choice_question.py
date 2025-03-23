import questionary

from instant_python.question_prompter.question.question import Question


class ChoiceQuestion(Question[str]):
    def __init__(self, key: str, message: str, options: list[str] | None = None) -> None:
        super().__init__(key, message)
        self._default = options[0] if options else ""
        self._options = options if options else []
    
    def ask(self) -> dict[str, str]:
        answer = questionary.select(
            self._message,
            choices=self._options,
            default=self._default,
        ).ask()
        return {self._key: answer}
