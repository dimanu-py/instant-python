from dataclasses import dataclass, field

import questionary

from src.question_prompter.question import Question


@dataclass(frozen=True)
class ChoiceQuestion(Question[str]):
	options: list[str] = field(default_factory=list)

	def ask(self) -> str:
		return questionary.select(
			self.message,
			choices=self.options,
			default=self.default,
		).ask()
