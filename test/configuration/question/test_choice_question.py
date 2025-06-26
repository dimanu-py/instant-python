from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, equal

from instant_python.configuration.question.choice_question import ChoiceQuestion
from instant_python.configuration.question.questionary import Questionary


class TestChoiceQuestion:
    def setup_method(self) -> None:
        self._questionary = Mimic(Mock, Questionary)
        self._question = ChoiceQuestion(
            key="test_key",
            message="Test message",
            options=["option1", "option2", "option3"],
            questionary=self._questionary,
        )

    def test_should_save_user_selection(self) -> None:
        self._given_user_selects_second_option()

        answer = self._question.ask()

        expect(answer).to(equal({"test_key": "option2"}))
        expect(self._questionary).to(have_been_satisfied)

    def _given_user_selects_second_option(self) -> None:
        expect_call(self._questionary).single_choice_question(
            "Test message", options=["option1", "option2", "option3"], default="option1"
        ).returns("option2")
