from instant_python.project_generator.folder_tree import FolderTree
from instant_python.project_generator.template_manager import TemplateManager


class ProjectGenerator:
    def __init__(self) -> None:
        self._folder_tree = FolderTree()
        self._template_manager = TemplateManager()

    def generate(self) -> None:
        raw_project_structure = self._template_manager.get_project("domain_driven_design")
        self._folder_tree.create(raw_project_structure)
