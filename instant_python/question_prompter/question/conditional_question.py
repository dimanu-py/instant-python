from instant_python.question_prompter.question.question import Question


class ConditionalQuestion:
    def __init__(
        self, base_question: Question, subquestions: list[Question], condition: str | bool
    ) -> None:
        self._base_question = base_question
        self._subquestions = subquestions
        self._condition = condition

    def ask(self) -> dict[str, str]:
        base_answer = self._base_question.ask()

        if base_answer != self._condition:
            return base_answer

        answers = base_answer
        for question in self._subquestions:
            answers.update(question.ask())
        return answers
