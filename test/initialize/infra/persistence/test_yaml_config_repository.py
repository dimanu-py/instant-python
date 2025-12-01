import json
import shutil
import tempfile
from pathlib import Path

from approvaltests import verify
from expects import expect, be_none, raise_error, be_true, equal

from instant_python.initialize.infra.persistence.yaml_config_repository import (
    YamlConfigRepository,
    ConfigurationFileNotFound,
)
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother
from test.utils import resources_path


class TestYamlConfigRepository:
    _CONFIG_FILE = "ipy.yml"

    def setup_method(self) -> None:
        self._repository = YamlConfigRepository()

    def test_should_write_and_read_valid_config_on_working_directory(self) -> None:
        config = ConfigSchemaMother.any()

        self._repository.write(config)

        saved_config = self._repository.read(config.config_file_path)
        expect(saved_config.to_primitives()).to(equal(config.to_primitives()))
        config.config_file_path.unlink()

    def test_should_raise_error_when_file_to_read_does_not_exist(self) -> None:
        config_path = Path("non/existing/path/config.yml")

        expect(lambda: self._repository.read(config_path)).to(raise_error(ConfigurationFileNotFound))

    def test_should_move_config_file_to_destination_folder(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            config = ConfigSchemaMother.with_config_path(temp_dir_path / self._CONFIG_FILE)
            project_folder = self._create_project_folder_in_temp_dir(temp_dir_path, config.project_folder_name)
            self._repository.write(config)

            self._repository.move(config, temp_dir_path)

            moved_config = self._repository.read(project_folder / self._CONFIG_FILE)
            expect(moved_config.to_primitives()).to(equal(config.to_primitives()))

    @staticmethod
    def _create_project_folder_in_temp_dir(temp_dir_path: Path, project_folder: str) -> Path:
        project_folder = temp_dir_path / project_folder
        project_folder.mkdir()
        return project_folder
