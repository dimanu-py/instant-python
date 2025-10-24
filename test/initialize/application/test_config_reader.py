from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, be_none

from instant_python.config.domain.config_parser import ConfigParser
from instant_python.initialize.application.config_reader import ConfigReader
from instant_python.initialize.domain.configuration_repository import ConfigurationRepository
from test.config.domain.mothers.configuration_schema_mother import ConfigurationSchemaMother


class TestConfigReader:
    def test_should_read_existing_configuration_from_file(self) -> None:
        configuration_repository = Mock(ConfigurationRepository)
        configuration_parser = Mock(ConfigParser)
        config_reader = ConfigReader(
            repository=configuration_repository,
            parser=configuration_parser,
        )
        config_file_path = "path/to/config/file.yml"
        config = ConfigurationSchemaMother.any()

        expect_call(configuration_repository).read_from_file(config_file_path).returns(config.to_primitives())
        expect_call(configuration_parser).parse(config.to_primitives()).returns(config)

        parsed_config = config_reader.execute(config_file_path)

        expect(parsed_config).to_not(be_none)
        expect(configuration_repository).to(have_been_satisfied)
        expect(configuration_parser).to(have_been_satisfied)
