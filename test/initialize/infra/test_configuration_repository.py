import json
from pathlib import Path

from approvaltests import verify
from expects import expect, be_none

from instant_python.initialize.infra.configuration_repository import YamlConfigurationRepository


class TestConfigurationRepository:
    def test_should_read_existing_config_file(self) -> None:
        repository = YamlConfigurationRepository()
        config_path = str(Path(__file__).parent / "resources" / "config.yml")

        raw_config = repository.read_from_file(config_path)

        expect(raw_config).to_not(be_none)
        verify(json.dumps(raw_config, indent=2))
