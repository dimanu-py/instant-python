from instant_python.configuration.question.choice_question import ChoiceQuestion
from instant_python.configuration.question.free_text_question import FreeTextQuestion
from instant_python.configuration.question.questionary import Questionary


class GeneralQuestionsStep:
    def __init__(self, questionary: Questionary) -> None:
        self._questions = [
            FreeTextQuestion(
                key="slug",
                message="Enter the name of the project (CANNOT CONTAIN SPACES)",
                default="python-project",
                questionary=questionary,
            ),
            FreeTextQuestion(
                key="source_name",
                message="Enter the name of the source folder",
                default="src",
                questionary=questionary,
            ),
            FreeTextQuestion(
                key="description",
                message="Enter the project description",
                default="Python Project Description",
                questionary=questionary,
            ),
            FreeTextQuestion(
                key="version",
                message="Enter the project initial version",
                default="0.1.0",
                questionary=questionary,
            ),
            FreeTextQuestion(
                key="author",
                message="Enter your name",
                questionary=questionary,
            ),
            ChoiceQuestion(
                key="license",
                message="Select a license",
                options=["MIT", "Apache", "GPL"],
                questionary=questionary,
            ),
            ChoiceQuestion(
                key="python_version",
                message="Enter the python version",
                options=["3.13", "3.12", "3.11", "3.10"],
                questionary=questionary,
            ),
            ChoiceQuestion(
                key="dependency_manager",
                message="Select a dependency manager",
                options=["uv", "pdm"],
                questionary=questionary,
            ),
        ]

    def run(self) -> dict[str, dict[str, str]]:
        answers = {}
        for question in self._questions:
            answers.update(question.ask())
        return {"general": answers}
