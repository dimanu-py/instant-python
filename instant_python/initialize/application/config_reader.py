from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.config_repository import ConfigRepository


class ConfigReader:
    def __init__(self, repository: ConfigRepository, parser: ConfigParser) -> None:
        self._repository = repository
        self._parser = parser

    def execute(self, config_file_path: str) -> ConfigSchema:
        raw_config = self._repository.read(config_file_path)
        configuration = self._parser.parse(raw_config, config_file_path)
        return configuration
