from instant_python.question_prompter.question.boolean_question import BooleanQuestion
from instant_python.question_prompter.question.free_text_question import FreeTextQuestion
from instant_python.question_prompter.step.steps import Step


class GitStep(Step):
    def __init__(self) -> None:
        self._questions = [
            BooleanQuestion(key="git", message="Do you want to initialize a git repository?", default=True),
            FreeTextQuestion(key="git_user_name", message="Type your git user name"),
            FreeTextQuestion(key="git_email", message="Type your git email"),
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        initialize_git_repo = self._questions[0].ask()
        answers_so_far[self._questions[0].key] = initialize_git_repo
        if not initialize_git_repo:
            return answers_so_far

        for question in self._questions[1:]:
            answers_so_far[question.key] = question.ask()
        return answers_so_far
