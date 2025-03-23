from instant_python.question_prompter.question.boolean_question import BooleanQuestion
from instant_python.question_prompter.question.conditional_question import ConditionalQuestion
from instant_python.question_prompter.question.free_text_question import FreeTextQuestion
from instant_python.question_prompter.step.steps import Step


class GitStep(Step):
    def __init__(self) -> None:
        self._questions = [
            ConditionalQuestion(
                base_question=BooleanQuestion(key="git", message="Do you want to initialize a git repository?", default=True),
                subquestions=[
                    FreeTextQuestion(key="git_user_name", message="Type your git user name"),
                    FreeTextQuestion(key="git_email", message="Type your git email"),
                ],
                condition=True
            )
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        for question in self._questions:
            answers_so_far.update(question.ask())
        return answers_so_far