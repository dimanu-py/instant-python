from src.question_prompter.question.free_text_question import FreeTextQuestion
from src.question_prompter.steps import Step
from src.question_prompter.template_types import TemplateTypes


class DomainDrivenDesignStep(Step):
    def __init__(self) -> None:
        self._questions = [
            FreeTextQuestion(
                key="bounded_context",
                message="Enter the bounded context name",
                default="backoffice",
            ),
            FreeTextQuestion(
                key="aggregate_name", message="Enter the aggregate name", default="user"
            ),
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        for question in self._questions:
            answers_so_far[question.key] = question.ask()

        return answers_so_far

    def should_not_ask(self, answers_so_far: dict[str, str]) -> bool:
        if answers_so_far["template"] != TemplateTypes.DDD:
            return True
        return False
