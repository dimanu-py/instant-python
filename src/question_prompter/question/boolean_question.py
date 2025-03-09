from dataclasses import dataclass, field

import questionary

from src.question_prompter.question.question import Question


@dataclass(frozen=True)
class BooleanQuestion(Question[bool]):
    default: bool = field(default=True)

    def ask(self) -> bool:
        return questionary.confirm(self.message, default=self.default).ask()
