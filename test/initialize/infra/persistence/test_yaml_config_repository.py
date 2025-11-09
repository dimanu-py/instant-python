import json
import shutil
import tempfile
from pathlib import Path

from approvaltests import verify
from expects import expect, be_none, raise_error, be_true

from instant_python.initialize.infra.persistence.yaml_config_repository import (
    YamlConfigRepository,
    ConfigurationFileNotFound,
)
from test.utils import resources_path


class TestYamlConfigRepository:
    _CONFIG_FILE = "base_ipy_config.yml"
    _A_PROJECT_NAME = "python-project"

    def test_should_read_existing_config_file(self) -> None:
        repository = YamlConfigRepository()
        config_path = resources_path() / self._CONFIG_FILE

        config = repository.read(config_path)

        expect(config).to_not(be_none)
        verify(json.dumps(config.to_primitives(), indent=2))

    def test_should_raise_error_when_file_to_read_does_not_exist(self) -> None:
        repository = YamlConfigRepository()
        config_path = Path("non/existing/path/config.yml")

        expect(lambda: repository.read(config_path)).to(raise_error(ConfigurationFileNotFound))

    def test_should_write_config_file_to_destination_folder(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            config_file_temp = self._create_config_file_in_temp_dir(temp_dir_path)
            project_folder = self._create_project_folder_in_temp_dir(temp_dir_path)

            repository = YamlConfigRepository()

            config = repository.read(config_file_temp)
            repository.move(config, temp_dir_path)

            final_config_path = project_folder / "ipy.yml"
            expect(final_config_path.exists()).to(be_true)
            expect(config_file_temp.exists()).to_not(be_true)

    def _create_project_folder_in_temp_dir(self, temp_dir_path: Path) -> Path:
        project_folder = temp_dir_path / self._A_PROJECT_NAME
        project_folder.mkdir()
        return project_folder

    def _create_config_file_in_temp_dir(self, temp_dir: Path) -> Path:
        config_file_source = resources_path() / self._CONFIG_FILE
        config_file_temp = temp_dir / self._CONFIG_FILE
        shutil.copy(config_file_source, config_file_temp)
        return config_file_temp
