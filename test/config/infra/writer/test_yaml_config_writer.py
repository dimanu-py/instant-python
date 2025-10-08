from pathlib import Path

from instant_python.config.infra.writer.yaml_config_writer import YamlConfigWriter
from test.config.domain.mothers.configuration_schema_mother import ConfigurationSchemaMother


class TestYamlConfigWriter:
    def test_should_save_valid_configuration(self) -> None:
        configuration = ConfigurationSchemaMother.any()
        config_writer = YamlConfigWriter()

        config_writer.write(configuration)

        expected_output_path = Path.cwd() / configuration._config_file_path
        assert expected_output_path.exists()
        expected_output_path.unlink()
