from pathlib import Path

import yaml

from instant_python.config.domain.config_writer import ConfigWriter
from instant_python.config.domain.configuration_schema import ConfigurationSchema


class YamlConfigWriter(ConfigWriter):
    def write(self, configuration: ConfigurationSchema) -> None:
        destination_folder = Path.cwd() / configuration.config_file_path
        with destination_folder.open("w") as file:
            yaml.dump(configuration.to_primitives(), file)
