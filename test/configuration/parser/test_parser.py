from pathlib import Path

from expects import expect, raise_error, be_none, be_empty, equal

from instant_python.configuration.config_key_not_present import ConfigKeyNotPresent
from instant_python.configuration.general.general_configuration import (
    GeneralConfiguration,
)
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

        expect(lambda: Parser.parse(config_file_path)).to(
            raise_error(ConfigurationFileNotFound)
        )

    def test_should_load_config_file_when_exists(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse(config_file_path)

        expect(config).to_not(be_none)

    def test_should_raise_error_if_config_file_is_empty(self) -> None:
        config_file_path = self._build_config_file_path("empty_config")

        expect(lambda: Parser.parse(config_file_path)).to(
            raise_error(EmptyConfigurationNotAllowed)
        )

    def test_should_raise_error_if_config_keys_are_not_present(self) -> None:
        config_file_path = self._build_config_file_path("missing_keys_config")

        expect(lambda: Parser.parse(config_file_path)).to(
            raise_error(ConfigKeyNotPresent)
        )

    def test_should_parse_general_configuration_key(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse(config_file_path)

        expected_general_config = GeneralConfiguration(
            slug="python-project",
            source_name="src",
            description="Python Project Description",
            version="0.1.0",
            author="Diego Martinez",
            license="MIT",
            python_version="3.13",
            dependency_manager="uv",
        )
        expect(config.general).to(equal(expected_general_config))

    def test_should_raise_error_if_general_configuration_has_missing_mandatory_fields(self) -> None:
        config_file_path = self._build_config_file_path("missing_general_fields_config")
        
        expect(lambda: Parser.parse(config_file_path)).to(
            raise_error(MissingMandatoryFields)
        )

    def test_should_parse_dependencies_configuration_key(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse(config_file_path)

        expect(config.dependencies).to_not(be_empty)
