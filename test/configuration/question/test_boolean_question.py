from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, equal

from instant_python.configuration.question.boolean_question import BooleanQuestion
from instant_python.configuration.question.questionary import Questionary


class TestBooleanQuestion:
    def setup_method(self) -> None:
        self._questionary = Mimic(Mock, Questionary)
        self._question = BooleanQuestion(
            key="test_key",
            message="Test message",
            default=False,
            questionary=self._questionary,
        )

    def test_should_save_user_response(self) -> None:
        self._given_answer_to_question_is_true()

        answer = self._question.ask()

        expect(answer).to(equal({"test_key": True}))
        expect(self._questionary).to(have_been_satisfied)

    def _given_answer_to_question_is_true(self) -> None:
        expect_call(self._questionary).boolean_question("Test message", default=False).returns(True)
