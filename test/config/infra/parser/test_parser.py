from expects import expect, raise_error

from instant_python.config.infra.parser.parser import Parser
from instant_python.configuration.parser.empty_configuration_not_allowed import EmptyConfigurationNotAllowed


class TestParser:
    def test_should_raise_error_if_answers_is_empty(self) -> None:
        parser = Parser()
        empty_answers = {}

        expect(lambda: parser.parse(empty_answers)).to(raise_error(EmptyConfigurationNotAllowed))
