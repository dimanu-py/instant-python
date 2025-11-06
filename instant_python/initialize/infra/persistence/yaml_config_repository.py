from pathlib import Path

import shutil
import yaml

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.configuration.parser.configuration_file_not_found import ConfigurationFileNotFound
from instant_python.initialize.domain.config_repository import ConfigRepository


class YamlConfigRepository(ConfigRepository):
    def read(self, path: Path) -> ConfigSchema:
        try:
            with path.open("r") as file:
                raw_config = yaml.safe_load(file)
                return ConfigSchema.from_primitives(content=raw_config, custom_config_path=path)
        except FileNotFoundError:
            raise ConfigurationFileNotFound(str(path))

    def write(self, config: ConfigSchema, destination_path: Path) -> None:
        final_destination = config.calculate_config_destination_path(
            destination_folder=destination_path,
        )
        shutil.move(config.config_file_path, final_destination)
