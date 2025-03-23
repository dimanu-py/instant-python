import subprocess

from instant_python.project_generator.folder_tree import FolderTree
from instant_python.project_generator.default_template_manager import TemplateManager


class ProjectGenerator:

    def __init__(self, folder_tree: FolderTree,
                 template_manager: TemplateManager) -> None:
        self._folder_tree = folder_tree
        self._template_manager = template_manager

    def generate(self) -> None:
        raw_project_structure = self._template_manager.get_project(
            template_name="project_structure")
        self._folder_tree.create(raw_project_structure)
        self._format_project_files()

    def _format_project_files(self) -> None:
        subprocess.run(
            "uvx ruff format",
            shell=True,
            check=True,
            cwd=self._folder_tree.project_directory,
            stdout=subprocess.DEVNULL,
        )

    @property
    def path(self) -> str:
        return self._folder_tree.project_directory
