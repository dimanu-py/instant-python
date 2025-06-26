from instant_python.configuration.question.boolean_question import BooleanQuestion
from instant_python.configuration.question.conditional_question import ConditionalQuestion
from instant_python.configuration.question.free_text_question import FreeTextQuestion
from instant_python.configuration.question.questionary import Questionary


class GitStep:
    def __init__(self, questionary: Questionary) -> None:
        self._questions = [
            ConditionalQuestion(
                base_question=BooleanQuestion(
                    key="initialize",
                    message="Do you want to initialize a git repository?",
                    default=True,
                    questionary=questionary,
                ),
                subquestions=[
                    FreeTextQuestion(key="username", message="Type your git user name", questionary=questionary),
                    FreeTextQuestion(key="email", message="Type your git email", questionary=questionary),
                ],
                condition=True,
            )
        ]

    def run(self) -> dict[str, dict[str, str | bool]]:
        answers = {}
        for question in self._questions:
            answers.update(question.ask())
        return {"git": answers}
