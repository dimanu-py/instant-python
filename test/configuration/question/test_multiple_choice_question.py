from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import equal, expect

from instant_python.configuration.question.multiple_choice_question import MultipleChoiceQuestion
from instant_python.configuration.question.questionary import Questionary


class TestMultipleChoiceQuestion:
    def setup_method(self) -> None:
        self._questionary = Mimic(Mock, Questionary)
        self._question = MultipleChoiceQuestion(
            key="test_key",
            message="Test message",
            options=["option1", "option2", "option3"],
            questionary=self._questionary,
        )

    def test_should_save_multiple_user_selections(self) -> None:
        self._given_user_selects_first_two_options()

        answer = self._question.ask()

        expect(answer).to(equal({"test_key": ["option1", "option2"]}))
        expect(self._questionary).to(have_been_satisfied)

    def _given_user_selects_first_two_options(self) -> None:
        expect_call(self._questionary).multiselect_question(
            "Test message",
            options=["option1", "option2", "option3"],
        ).returns(["option1", "option2"])
