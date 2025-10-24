import json
from pathlib import Path

from approvaltests import verify
from expects import expect, be_none, raise_error

from instant_python.configuration.parser.configuration_file_not_found import ConfigurationFileNotFound
from instant_python.initialize.infra.configuration_repository import YamlConfigurationRepository


class TestConfigurationRepository:
    def test_should_read_existing_config_file(self) -> None:
        repository = YamlConfigurationRepository()
        config_path = str(Path(__file__).parent / "resources" / "config.yml")

        raw_config = repository.read_from_file(config_path)

        expect(raw_config).to_not(be_none)
        verify(json.dumps(raw_config, indent=2))

    def test_should_raise_error_when_file_to_read_does_not_exist(self) -> None:
        repository = YamlConfigurationRepository()
        config_path = "non/existing/path/config.yml"

        expect(lambda: repository.read_from_file(config_path)).to(raise_error(ConfigurationFileNotFound))
