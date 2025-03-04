import questionary

from src.question_prompter.question import Question
from src.question_prompter.questions_definition import (
    GENERAL_QUESTIONS,
    DDD_QUESTIONS,
)
from src.question_prompter.template_types import TemplateTypes
from src.question_prompter.user_requirements import UserRequirements


class BasicPrompter:
    @staticmethod
    def ask() -> UserRequirements:
        answers = {
            question.key: question.ask()
            for question in GENERAL_QUESTIONS
        }

        if answers["template"] == TemplateTypes.DDD:
            ddd_answers = {
                question.key: question.ask()
                for question in DDD_QUESTIONS
            }
            answers.update(ddd_answers)

        return UserRequirements(**answers)
