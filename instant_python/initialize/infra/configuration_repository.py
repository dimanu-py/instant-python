from pathlib import Path

import yaml

from instant_python.initialize.domain.configuration_repository import ConfigurationRepository


class YamlConfigurationRepository(ConfigurationRepository):
    def read_from_file(self, path: str) -> dict:
        with Path(path).open("r") as file:
            return yaml.safe_load(file)
