from instant_python.initialize.domain.configuration_repository import ConfigurationRepository


class YamlConfigurationRepository(ConfigurationRepository):
    def read_from_file(self, path: str) -> dict:
        pass
