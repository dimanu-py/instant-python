from typing import Union

from instant_python.question_prompter.question.question import Question


class ConditionalQuestion:
    def __init__(
        self, base_question: Question, subquestions: Union[list[Question], "ConditionalQuestion"], condition: str | bool
    ) -> None:
        self._base_question = base_question
        self._subquestions = subquestions
        self._condition = condition

    def ask(self) -> dict[str, str]:
        base_answer = self._base_question.ask()

        if self._base_answer_does_not_satisfies_condition(base_answer):
            return base_answer

        answers = base_answer
        
        if isinstance(self._subquestions, ConditionalQuestion):
            answers.update(self._subquestions.ask())
        else:
            for question in self._subquestions:
                answers.update(question.ask())
        return answers

    def _base_answer_does_not_satisfies_condition(self, base_answer: dict[str, str]) -> bool:
        answer_value = next(iter(base_answer.values()))
        return answer_value != self._condition
