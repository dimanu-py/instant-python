from pathlib import Path

import yaml
from expects import expect, raise_error

from instant_python.config.infra.parser.parser import Parser
from instant_python.configuration.parser.config_key_not_present import ConfigKeyNotPresent
from instant_python.configuration.parser.empty_configuration_not_allowed import EmptyConfigurationNotAllowed


class TestParser:
    def test_should_raise_error_if_answers_is_empty(self) -> None:
        parser = Parser()
        empty_answers = {}

        expect(lambda: parser.parse(empty_answers)).to(raise_error(EmptyConfigurationNotAllowed))

    def test_should_raise_error_if_some_section_is_missing(self) -> None:
        parser = Parser()
        answers = self._read_fake_answers_from_file("missing_keys_answers")

        expect(lambda: parser.parse(answers)).to(raise_error(ConfigKeyNotPresent))

    @staticmethod
    def _read_fake_answers_from_file(file_name: str) -> dict[str, dict]:
        with open(Path(__file__).parent / "resources" / f"{file_name}.yml") as answers:
            return yaml.safe_load(answers)