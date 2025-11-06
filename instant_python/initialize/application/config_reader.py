from pathlib import Path

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.config_repository import ConfigRepository


class ConfigReader:
    def __init__(self, repository: ConfigRepository) -> None:
        self._repository = repository

    def execute(self, config_file_path: str) -> ConfigSchema:
        return self._repository.read(Path(config_file_path))
