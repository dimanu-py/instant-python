import questionary

from instant_python.question_prompter.question.boolean_question import BooleanQuestion
from instant_python.question_prompter.question.free_text_question import FreeTextQuestion
from instant_python.question_prompter.step.steps import Step


class GitStep(Step):
    def __init__(self) -> None:
        self._questions = [
            BooleanQuestion(
                key="continue_git",
                message="You've selected to initialize a git repository, do you want to specify"
                " your git user name and email for the project?",
                default=True,
            ),
            FreeTextQuestion(key="git_user_name", message="Type your git user name"),
            FreeTextQuestion(key="git_email", message="Type your git email"),
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        continue_git = self._questions[0].ask()
        if not continue_git:
            return answers_so_far

        for question in self._questions[1:]:
            answers_so_far[question.key] = question.ask()
        return answers_so_far

    def should_not_ask(self, answers_so_far: dict[str, str]) -> bool:
        if answers_so_far["git"]:
            return False
        return True
