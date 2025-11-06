from pathlib import Path

import yaml

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.configuration.parser.configuration_file_not_found import ConfigurationFileNotFound
from instant_python.initialize.domain.config_repository import ConfigRepository


class YamlConfigRepository(ConfigRepository):
    def read(self, path: str) -> ConfigSchema:
        try:
            with Path(path).open("r") as file:
                raw_config = yaml.safe_load(file)
                return ConfigSchema.from_primitives(content=raw_config, custom_config_path=path)
        except FileNotFoundError:
            raise ConfigurationFileNotFound(path)
