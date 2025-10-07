from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.configuration_schema import ConfigurationSchema
from instant_python.configuration.parser.config_key_not_present import ConfigKeyNotPresent
from instant_python.configuration.parser.empty_configuration_not_allowed import EmptyConfigurationNotAllowed


class Parser(ConfigParser):
    _REQUIRED_CONFIG_KEYS = ["general", "dependencies", "template", "git"]

    def parse(self, content: dict[str, dict]) -> ConfigurationSchema:
        if not content:
            raise EmptyConfigurationNotAllowed

        missing_keys = [key for key in self._REQUIRED_CONFIG_KEYS if key not in content]
        if missing_keys:
            raise ConfigKeyNotPresent(missing_keys, self._REQUIRED_CONFIG_KEYS)
