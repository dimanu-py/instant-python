from src.question_prompter.question.boolean_question import BooleanQuestion
from src.question_prompter.question.choice_question import ChoiceQuestion
from src.question_prompter.question.free_text_question import FreeTextQuestion
from src.question_prompter.steps import Step


class GeneralProjectStep(Step):
    def __init__(self) -> None:
        self._questions = [
            FreeTextQuestion(
                key="project_name",
                message="Enter the name of the project",
                default="Python Project",
            ),
            FreeTextQuestion(
                key="project_slug",
                message="Enter the slug of the project",
                default="python-project",
            ),
            FreeTextQuestion(
                key="source_name",
                message="Enter the name of the source folder",
                default="src",
            ),
            FreeTextQuestion(
                key="description",
                message="Enter the project description",
                default="Python Project Description",
            ),
            FreeTextQuestion(
                key="version",
                message="Enter the project initial version",
                default="0.1.0",
            ),
            FreeTextQuestion(key="author", message="Enter your name"),
            FreeTextQuestion(key="email", message="Enter your email"),
            ChoiceQuestion(
                key="license",
                message="Select a license",
                default="MIT",
                options=["MIT", "Apache", "GPL"],
            ),
	        BooleanQuestion(key="git", message="Do you want to initialize a git repository?"),
	        ChoiceQuestion(
                key="template",
                message="Select a template",
                default="domain_driven_design",
                options=["domain_driven_design", "clean_architecture", "empty_project"],
            ),
        ]

    def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
        for question in self._questions:
            answers_so_far[question.key] = question.ask()
        return answers_so_far

    def should_not_ask(self, answers_so_far: dict[str, str]) -> bool:
        return False
