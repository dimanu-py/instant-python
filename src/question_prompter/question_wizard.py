from src.question_prompter.step.steps import Steps
from src.question_prompter.user_requirements import UserRequirements


class QuestionWizard:
    def __init__(self, steps: Steps) -> None:
        self._steps = steps
        self._answers = {}

    def run(self) -> UserRequirements:
        for step in self._steps:
            if step.should_not_ask(self._answers):
                continue
            answer = step.run(self._answers)
            self._answers.update(answer)

        return UserRequirements(**self._answers)
