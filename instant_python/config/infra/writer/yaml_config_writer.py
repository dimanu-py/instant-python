from instant_python.config.domain.config_writer import ConfigWriter
from instant_python.config.domain.configuration_schema import ConfigurationSchema


class YamlConfigWriter(ConfigWriter):
    def write(self, configuration: ConfigurationSchema) -> None:
        raise NotImplementedError()
