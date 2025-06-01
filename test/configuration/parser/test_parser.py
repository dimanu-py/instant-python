from expects import expect, raise_error

from instant_python.configuration.parser.configuration_file_not_found import ConfigurationFileNotFound
from instant_python.configuration.parser.parser import Parser


class TestParser:
    def test_should_raise_error_if_config_file_is_not_found(self) -> None:
        config_file_path = "non_existent_config_file.yml"

        expect(lambda: Parser.parse(config_file_path)).to(
            raise_error(ConfigurationFileNotFound)
        )
