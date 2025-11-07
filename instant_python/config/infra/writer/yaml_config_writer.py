from pathlib import Path

import yaml

from instant_python.config.domain.config_writer import ConfigWriter
from instant_python.shared.domain.config_schema import ConfigSchema


class YamlConfigWriter(ConfigWriter):
    def write(self, config: ConfigSchema) -> None:
        destination_folder = Path.cwd() / config.config_file_path
        with destination_folder.open("w") as file:
            yaml.dump(config.to_primitives(), file)
