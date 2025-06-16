import json
import shutil
from pathlib import Path

from approvaltests import verify

from instant_python.project_creator.file_system import FileSystem
from instant_python.render.jinja_environment import JinjaEnvironment


class TestFileSystem:
    def setup_method(self) -> None:
        self.jinja_environment = JinjaEnvironment(package_name="test", template_directory="project_creator/resources")
        self.file_system = FileSystem(jinja_environment=self.jinja_environment)

    def teardown_method(self) -> None:
        project_folder = Path("python-project")
        if project_folder.exists():
            shutil.rmtree(project_folder)

    def test_should_create_folders_and_files(self) -> None:
        project_structure = self._load_project_structure()

        self.file_system.create_folders_and_files(
            project_structure=project_structure,
        )

        verify(self.file_system)

    def _get_file_structure(self, path: Path) -> dict:
        project_file_system = {}
        for child in sorted(path.iterdir(), key=lambda folder: folder.name):
            if child.is_dir():
                project_file_system[child.name] = self._get_file_structure(child)
            else:
                project_file_system[child.name] = child.read_text()
        return project_file_system

    @staticmethod
    def _load_project_structure() -> list[dict[str, list[str] | str | bool]]:
        with open(Path(__file__).parent / "resources" / "rendered_project_structure.json", "r") as file:
            return json.load(file)
