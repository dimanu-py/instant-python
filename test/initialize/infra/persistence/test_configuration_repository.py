import json

from approvaltests import verify
from expects import expect, be_none, raise_error

from instant_python.configuration.parser.configuration_file_not_found import ConfigurationFileNotFound
from instant_python.initialize.infra.persistence.config_repository import YamlConfigRepository
from test.initialize.delivery.test_init_cli import test_resources_path


class TestConfigurationRepository:
    def test_should_read_existing_config_file(self) -> None:
        repository = YamlConfigRepository()
        config_path = str(test_resources_path() / "base_ipy_config.yml")

        raw_config = repository.read(config_path)

        expect(raw_config).to_not(be_none)
        verify(json.dumps(raw_config, indent=2))

    def test_should_raise_error_when_file_to_read_does_not_exist(self) -> None:
        repository = YamlConfigRepository()
        config_path = "non/existing/path/config.yml"

        expect(lambda: repository.read(config_path)).to(raise_error(ConfigurationFileNotFound))
