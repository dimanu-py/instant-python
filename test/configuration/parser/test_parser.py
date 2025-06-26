import json
from pathlib import Path

import pytest
from approvaltests import verify
from expects import expect, raise_error, be_none

from instant_python.configuration.parser.config_key_not_present import ConfigKeyNotPresent
from instant_python.configuration.parser.configuration_file_not_found import (
    ConfigurationFileNotFound,
)
from instant_python.configuration.parser.empty_configuration_not_allowed import (
    EmptyConfigurationNotAllowed,
)
from instant_python.configuration.parser.missing_mandatory_fields import MissingMandatoryFields
from instant_python.configuration.parser.parser import Parser


class TestParser:
    @staticmethod
    def _build_config_file_path(file_name: str) -> str:
        return str(Path(__file__).parent / "resources" / f"{file_name}.yml")

    def test_should_raise_error_if_config_file_is_not_found(self) -> None:
        config_file_path = "non_existent_config_file"

        expect(lambda: Parser.parse_from_file(config_file_path)).to(raise_error(ConfigurationFileNotFound))

    def test_should_load_config_file_when_exists(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse_from_file(config_file_path)

        expect(config).to_not(be_none)

    def test_should_raise_error_if_config_file_is_empty(self) -> None:
        config_file_path = self._build_config_file_path("empty_config")

        expect(lambda: Parser.parse_from_file(config_file_path)).to(raise_error(EmptyConfigurationNotAllowed))

    def test_should_raise_error_if_config_keys_are_not_present(self) -> None:
        config_file_path = self._build_config_file_path("missing_keys_config")

        expect(lambda: Parser.parse_from_file(config_file_path)).to(raise_error(ConfigKeyNotPresent))

    @pytest.mark.parametrize(
        "file_name",
        [
            pytest.param("missing_general_fields_config", id="missing_general_fields"),
            pytest.param("missing_dependencies_fields_config", id="missing_dependencies_fields"),
            pytest.param("missing_git_fields_config", id="missing_git_fields"),
            pytest.param("missing_template_fields_config", id="missing_template_fields"),
        ],
    )
    def test_should_raise_error_when_mandatory_fields_are_missing_in_configuration(self, file_name: str) -> None:
        config_file_path = self._build_config_file_path(file_name)

        expect(lambda: Parser.parse_from_file(config_file_path)).to(raise_error(MissingMandatoryFields))

    def test_should_parse_configuration(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse_from_file(config_file_path)

        config_json = json.dumps(config.to_primitives(), indent=2, sort_keys=True)
        verify(config_json)
