from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, equal

from instant_python.configuration.question.free_text_question import FreeTextQuestion
from instant_python.configuration.question.questionary import Questionary


class TestFreeTextQuestion:
    def setup_method(self) -> None:
        self._questionary = Mimic(Mock, Questionary)
        self._question = FreeTextQuestion(
            key="test_key",
            message="Test message",
            default="default answer",
            questionary=self._questionary,
        )

    def test_should_save_user_input_answer(self) -> None:
        self._given_user_writes_free_answer()

        answer = self._question.ask()

        expect(answer).to(equal({"test_key": "user input answer"}))
        expect(self._questionary).to(have_been_satisfied)

    def _given_user_writes_free_answer(self) -> None:
        expect_call(self._questionary).free_text_question("Test message", default="default answer").returns(
            "user input answer"
        )
