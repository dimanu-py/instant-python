from src.project_generator.folder_tree import FolderTree
from src.project_generator.template_manager import TemplateManager


class ProjectGenerator:
    def __init__(self) -> None:
        self._folder_tree = FolderTree()
        self._template_manager = TemplateManager()

    def generate(self) -> None:
        raw_project_structure = self._template_manager.get_project(template_name="project_structure")
        self._folder_tree.create(raw_project_structure)
