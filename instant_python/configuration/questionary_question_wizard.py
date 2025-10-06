from instant_python.config.domain.question_wizard import QuestionWizard
from instant_python.configuration.step.steps import Steps


class QuestionaryQuestionWizard(QuestionWizard):
    def __init__(self, steps: Steps) -> None:
        self._steps = steps
        self._answers = {}

    def run(self) -> dict:
        for step in self._steps:
            answer = step.run()
            self._answers.update(answer)

        return self._answers
