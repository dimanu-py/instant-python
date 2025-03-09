from dataclasses import dataclass

from src.question_prompter.question.boolean_question import BooleanQuestion
from src.question_prompter.question.free_text_question import FreeTextQuestion
from src.question_prompter.question.question import Question


@dataclass(frozen=True)
class DependenciesQuestion(Question[list[str]]):
	def ask(self) -> list[str]:
		dependencies = []
		while True:
			user_wants_to_install_dependencies = BooleanQuestion(
				key="keep_asking", message=self.message, default=False
			).ask()

			if not user_wants_to_install_dependencies:
				break

			dependency = FreeTextQuestion(
				key="dependency",
				message="Enter the name of the dependency you want to install",
			).ask()

			if not dependency:
				print("Dependency name cannot be empty. Let's try again.")
				continue

			dependency_is_correct = BooleanQuestion(
				key="dependency_is_correct",
				message=f"Is '{dependency}' spelled correctly?",
				default=True,
			).ask()

			if dependency_is_correct:
				print(f"Dependency {dependency} will be installed.")
				dependencies.append(dependency)
			else:
				print("Let's try again.")

		return dependencies
