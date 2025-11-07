from pathlib import Path

from instant_python.config.infra.writer.yaml_config_writer import YamlConfigWriter
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother


class TestYamlConfigWriter:
    def test_should_save_valid_config(self) -> None:
        config = ConfigSchemaMother.any()
        config_writer = YamlConfigWriter()

        config_writer.write(config)

        expected_output_path = Path.cwd() / config.config_file_path
        assert expected_output_path.exists()
        expected_output_path.unlink()
