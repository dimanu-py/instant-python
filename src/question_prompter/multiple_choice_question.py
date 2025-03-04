from dataclasses import dataclass, field

import questionary

from src.question_prompter.question import Question


@dataclass(frozen=True)
class MultipleChoiceQuestion(Question[list[str]]):
    options: list[str] = field(default_factory=list)

    def ask(self) -> list[str]:
        return questionary.checkbox(self.message, choices=self.options).ask()
