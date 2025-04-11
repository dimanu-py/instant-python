from instant_python.question_prompter.step.steps import Steps
from instant_python.question_prompter.requirements_configuration import RequirementsConfiguration


class QuestionWizard:
    def __init__(self, steps: Steps) -> None:
        self._steps = steps
        self._answers = {}

    def run(self) -> RequirementsConfiguration:
        for step in self._steps:
            answer = step.run(self._answers)
            self._answers.update(answer)

        return RequirementsConfiguration(**self._answers)
