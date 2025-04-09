import yaml
from jinja2 import Template

from instant_python.project_generator.jinja_environment import JinjaEnvironment
from instant_python.project_generator.template_manager import TemplateManager
from instant_python.question_prompter.template_types import TemplateTypes
from instant_python.question_prompter.requirements_configuration import RequirementsConfiguration


class JinjaTemplateManager(TemplateManager):

    def __init__(self) -> None:
        self._requirements = self._load_memory_requirements()
        self._env = JinjaEnvironment()

    def get_project(self, template_name: str) -> dict:
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
        return template.render(**self._requirements.to_dict(), template_types=TemplateTypes)

    @staticmethod
    def _load_memory_requirements() -> UserRequirements:
        with open("user_requirements.yml") as file:
    def _load_memory_requirements() -> RequirementsConfiguration:
            requirements = yaml.safe_load(file)
        return RequirementsConfiguration(**requirements)
