import json
import shutil
from pathlib import Path

import pytest
from approvaltests import verify
from approvaltests.namer import NamerFactory

from instant_python.configuration.parser.parser import Parser
from instant_python.project_creator.file_system import FileSystem
from instant_python.render.jinja_environment import JinjaEnvironment


class TestFileSystem:
    def test_should_generate_file_system_tree(self) -> None:
        project_structure = self._load_project_structure("rendered_project_structure.json")

        file_system = FileSystem(project_structure=project_structure)

        verify(file_system)

    @pytest.mark.parametrize(
        "project_structure_file_name, config_file",
        [
            pytest.param("rendered_project_structure.json", "config.yml", id="base_project_structure"),
            pytest.param("rendered_custom_project_structure.json", "config.yml", id="custom_project_structure"),
            pytest.param(
                "rendered_project_structure_only_with_fastapi.json",
                "config_with_only_fastapi.yml",
                id="only_fastapi_project_structure",
            ),
            pytest.param(
                "rendered_project_structure_fastapi_with_logger.json",
                "config_fastapi_with_logger.yml",
                id="fastapi_with_logger_project_structure",
            ),
            pytest.param(
                "rendered_project_structure_fastapi_with_migrator.json",
                "config_fastapi_with_migrator.yml",
                id="fastapi_with_migrator_project_structure",
            ),
        ],
    )
    def test_should_create_file_system_in_disk(self, project_structure_file_name: str, config_file: str) -> None:
        project_structure = self._load_project_structure(project_structure_file_name)
        file_renderer = JinjaEnvironment(package_name="test", template_directory="project_creator/resources")
        configuration = Parser.parse_from_file(str(Path(__file__).parent / "resources" / config_file))

        file_system = FileSystem(project_structure=project_structure)
        file_system.write_on_disk(file_renderer=file_renderer, context=configuration)

        project_file_system = self._get_file_structure(Path(configuration.project_folder_name))
        self._clean_up_created_project(Path(configuration.project_folder_name))
        verify(project_file_system, options=NamerFactory.with_parameters(project_structure_file_name))

    def _get_file_structure(self, path: Path) -> dict:
        project_file_system = {}
        for child in sorted(path.iterdir(), key=lambda folder: folder.name):
            if child.is_dir():
                project_file_system[child.name] = self._get_file_structure(child)
            else:
                project_file_system[child.name] = child.read_text()
        return project_file_system

    @staticmethod
    def _load_project_structure(project_structure_file_name: str) -> list[dict[str, list[str] | str | bool]]:
        with open(Path(__file__).parent / "resources" / project_structure_file_name, "r") as file:
            return json.load(file)

    @staticmethod
    def _clean_up_created_project(project_path: Path) -> None:
        if project_path.exists():
            shutil.rmtree(project_path)
