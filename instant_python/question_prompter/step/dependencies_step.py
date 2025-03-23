from instant_python.question_prompter.question.choice_question import ChoiceQuestion
from instant_python.question_prompter.question.dependencies_question import DependenciesQuestion
from instant_python.question_prompter.question.multiple_choice_question import MultipleChoiceQuestion
from instant_python.question_prompter.step.steps import Step


class DependenciesStep(Step):
    def __init__(self) -> None:
        self._questions = [
            DependenciesQuestion(
                key="dependencies",
                message="Do you want to install any dependencies?",
            )
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        for question in self._questions:
            answers_so_far[question.key] = question.ask()

        return answers_so_far

    def should_not_ask(self, answers_so_far: dict[str, str]) -> bool:
        return False
