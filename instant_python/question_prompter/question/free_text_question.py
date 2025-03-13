from dataclasses import dataclass

import questionary

from instant_python.question_prompter.question.question import Question


@dataclass(frozen=True)
class FreeTextQuestion(Question[str]):
    def ask(self) -> str:
        return questionary.text(self.message, default=self.default).ask()
