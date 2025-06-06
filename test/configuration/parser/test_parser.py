from pathlib import Path

import pytest
from expects import expect, raise_error, be_none, equal

from instant_python.configuration.parser.config_key_not_present import ConfigKeyNotPresent
from instant_python.configuration.dependency.dependency_configuration import DependencyConfiguration
from instant_python.configuration.general.general_configuration import (
    GeneralConfiguration,
)
from instant_python.configuration.git.git_configuration import GitConfiguration
from instant_python.configuration.parser.configuration_file_not_found import (
    ConfigurationFileNotFound,
)
from instant_python.configuration.parser.empty_configuration_not_allowed import (
    EmptyConfigurationNotAllowed,
)
from instant_python.configuration.parser.missing_mandatory_fields import MissingMandatoryFields
from instant_python.configuration.parser.parser import Parser
from instant_python.configuration.template.template_configuration import TemplateConfiguration


class TestParser:
    @staticmethod
    def _build_config_file_path(file_name: str) -> str:
        return str(Path(__file__).parent / "resources" / f"{file_name}.yml")

    def test_should_raise_error_if_config_file_is_not_found(self) -> None:
        config_file_path = "non_existent_config_file"

        expect(lambda: Parser.parse(config_file_path)).to(raise_error(ConfigurationFileNotFound))

    def test_should_load_config_file_when_exists(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse(config_file_path)

        expect(config).to_not(be_none)

    def test_should_raise_error_if_config_file_is_empty(self) -> None:
        config_file_path = self._build_config_file_path("empty_config")

        expect(lambda: Parser.parse(config_file_path)).to(raise_error(EmptyConfigurationNotAllowed))

    def test_should_raise_error_if_config_keys_are_not_present(self) -> None:
        config_file_path = self._build_config_file_path("missing_keys_config")

        expect(lambda: Parser.parse(config_file_path)).to(raise_error(ConfigKeyNotPresent))

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

    def test_should_parse_dependencies_configuration_key(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse(config_file_path)

        expected_dependencies = [
            DependencyConfiguration(
                name="pytest",
                version="latest",
                is_dev=True,
                group="test",
            ),
            DependencyConfiguration(
                name="fastapi",
                version="latest",
                is_dev=False,
            ),
        ]
        expect(config.dependencies).to(equal(expected_dependencies))

    def test_should_parse_git_configuration_key(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse(config_file_path)

        expected_git_config = GitConfiguration(
            initialize=True,
            username="dimanu-py",
            email="dimanu.py@gmail.com",
        )
        expect(config.git).to(equal(expected_git_config))

    def test_should_parse_template_config(self) -> None:
        config_file_path = self._build_config_file_path("config")

        config = Parser.parse(config_file_path)

        expected_template_config = TemplateConfiguration(
            name="domain_driven_design",
            built_in_features=[],
            specify_bounded_context=False,
            bounded_context=None,
            aggregate_name=None,
        )
        expect(config.template).to(equal(expected_template_config))

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

        expect(lambda: Parser.parse(config_file_path)).to(raise_error(MissingMandatoryFields))
