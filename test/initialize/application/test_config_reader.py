from pathlib import Path

from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, be_none

from instant_python.initialize.application.config_reader import ConfigReader
from instant_python.initialize.domain.config_repository import ConfigRepository
from test.config.domain.mothers.config_schema_mother import ConfigSchemaMother


class TestConfigReader:
    def test_should_read_existing_configuration_from_file(self) -> None:
        configuration_repository = Mock(ConfigRepository)
        config_reader = ConfigReader(repository=configuration_repository)
        config_file_path = Path("path/to/config/file.yml")
        config = ConfigSchemaMother.any()

        expect_call(configuration_repository).read(config_file_path).returns(config.to_primitives())

        parsed_config = config_reader.execute(config_file_path)

        expect(parsed_config).to_not(be_none)
        expect(configuration_repository).to(have_been_satisfied)
