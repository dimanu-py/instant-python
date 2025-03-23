from instant_python.question_prompter.question.choice_question import ChoiceQuestion
from instant_python.question_prompter.question.free_text_question import FreeTextQuestion
from instant_python.question_prompter.step.steps import Step


class GeneralCustomTemplateProjectStep(Step):
	def __init__(self) -> None:
		self._questions = [
			FreeTextQuestion(
				key="project_slug",
				message="Enter the name of the project (CANNOT CONTAIN SPACES)",
				default="python-project",
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
			ChoiceQuestion(
				key="license",
				message="Select a license",
				options=["MIT", "Apache", "GPL"],
			),
			ChoiceQuestion(
				key="python_version",
				message="Enter the python version",
				options=["3.13", "3.12", "3.11", "3.10"],
			),
			ChoiceQuestion(
				key="dependency_manager",
				message="Select a dependency manager",
				options=["uv", "pdm"],
			),
		]

	def run(self, answers_so_far: dict[str, str]) -> dict[str, str]:
		for question in self._questions:
			answers_so_far.update(question.ask())
		return answers_so_far
