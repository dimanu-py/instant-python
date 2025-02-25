import yaml
from jinja2 import Environment, FileSystemLoader, Template

from instant_python.project_generator.folder_tree import FolderTree
from instant_python.question_prompter.user_requirements import UserRequirements


class ProjectGenerator:
    def __init__(self, requirements: UserRequirements) -> None:
        self._folder_tree = FolderTree()
        self._requirements = requirements
        self._jinja_env = Environment(loader=FileSystemLoader("templates"))

    def generate(self) -> None:
        if self._is_ddd_project():
            template = self._jinja_env.get_template(
                "domain_driven_design/main_structure.yml.j2"
            )

        raw_project_structure = self._render(template)
        self._folder_tree.create(raw_project_structure)

    def _render(self, template: Template) -> dict:
        rendered_template = template.render(**self._requirements.to_dict())
        return yaml.safe_load(rendered_template)

    def _is_ddd_project(self) -> bool:
        return self._requirements.template == "DDD"
