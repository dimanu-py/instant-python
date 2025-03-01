import yaml
from jinja2 import FileSystemLoader, Environment, Template

from src.project_generator.jinja_custom_filters import is_in
from src.question_prompter.template_types import TemplateTypes
from src.question_prompter.user_requirements import UserRequirements


class TemplateManager:
    def __init__(self) -> None:
        self._requirements = self._load_memory_requirements()
        self._env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True)
        self._env.filters["is_in"] = is_in

    def get_project(self, template_name: str) -> dict:
        if self._is_ddd_project():
            template = self._get_template(
                f"{template_name}/{self._requirements.template}/main_structure.yml.j2"
            )
        raw_project_structure = self._render(template)
        return yaml.safe_load(raw_project_structure)

    def get_boilerplate(self, template_name: str) -> str:
        template = self._get_template(f"{template_name}")
        return self._render(template)

    def _get_template(self, name: str) -> Template:
        return self._env.get_template(name)

    def _render(self, template: Template) -> str:
        return template.render(**self._requirements.to_dict())

    def _is_ddd_project(self) -> bool:
        return self._requirements.template == TemplateTypes.DDD

    @staticmethod
    def _load_memory_requirements() -> UserRequirements:
        with open("user_requirements.yml") as file:
            requirements = yaml.safe_load(file)
        return UserRequirements(**requirements)
