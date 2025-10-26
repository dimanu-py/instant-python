from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.configuration_repository import ConfigurationRepository


class ConfigReader:
    def __init__(self, repository: ConfigurationRepository, parser: ConfigParser) -> None:
        self._repository = repository
        self._parser = parser

    def execute(self, config_file_path: str) -> ConfigSchema:
        raw_config = self._repository.read(config_file_path)
        configuration = self._parser.parse(raw_config, config_file_path)
        return configuration
