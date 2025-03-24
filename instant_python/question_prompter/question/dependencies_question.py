from instant_python.question_prompter.question.boolean_question import BooleanQuestion
from instant_python.question_prompter.question.free_text_question import (
    FreeTextQuestion,
)
from instant_python.question_prompter.question.question import Question


class DependenciesQuestion(Question[list[str]]):
    def __init__(self, key: str, message: str) -> None:
        super().__init__(key, message)

    def ask(self) -> dict[str, list[str]]:
        dependencies = []
        while True:
            user_wants_to_install_dependencies = BooleanQuestion(
                key="keep_asking", message=self._message, default=False
            ).ask()["keep_asking"]

            if not user_wants_to_install_dependencies:
                break

            dependency = FreeTextQuestion(
                key="dependency",
                message="Enter the name of the dependency you want to install",
            ).ask()["dependency"]

            if not dependency:
                print("Dependency name cannot be empty. Let's try again.")
                continue

            dependency_is_correct = BooleanQuestion(
                key="dependency_is_correct",
                message=f"Is '{dependency}' spelled correctly?",
                default=True,
            ).ask()["dependency_is_correct"]

            if dependency_is_correct:
                print(f"Dependency {dependency} will be installed.")
                dependencies.append(dependency)
            else:
                print("Let's try again.")

        return {self._key: dependencies}
