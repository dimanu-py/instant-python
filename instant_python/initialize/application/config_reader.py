from instant_python.config.domain.config_parser import ConfigParser
from instant_python.initialize.domain.configuration_repository import ConfigurationRepository


class ConfigReader:
    def __init__(self, repository: ConfigurationRepository, parser: ConfigParser) -> None:
        self._repository = repository
        self._parser = parser

    def execute(self, config_file_path: str) -> None:
        raise NotImplementedError()
