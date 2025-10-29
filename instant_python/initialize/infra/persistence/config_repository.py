from pathlib import Path

import yaml

from instant_python.configuration.parser.configuration_file_not_found import ConfigurationFileNotFound
from instant_python.initialize.domain.config_repository import ConfigRepository


class YamlConfigRepository(ConfigRepository):
    def read(self, path: str) -> dict:
        try:
            with Path(path).open("r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise ConfigurationFileNotFound(path)
