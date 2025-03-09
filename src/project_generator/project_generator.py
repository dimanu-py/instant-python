from src.project_generator.folder_tree import FolderTree
from src.project_generator.template_manager import TemplateManager


class ProjectGenerator:
    def __init__(
        self, folder_tree: FolderTree, template_manager: TemplateManager
    ) -> None:
        self._folder_tree = folder_tree
        self._template_manager = template_manager

    def generate(self) -> None:
        raw_project_structure = self._template_manager.get_project(
            template_name="project_structure"
        )
        self._folder_tree.create(raw_project_structure)

    @property
    def path(self) -> str:
        return self._folder_tree.project_directory
