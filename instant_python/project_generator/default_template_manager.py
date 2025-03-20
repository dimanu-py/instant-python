import yaml
from jinja2 import Environment, Template, PackageLoader

from instant_python.project_generator.jinja_custom_filters import is_in
from instant_python.question_prompter.user_requirements import UserRequirements


class DefaultTemplateManager:
    def __init__(self) -> None:
        self._requirements = self._load_memory_requirements()
        self._env = Environment(loader=PackageLoader("instant_python", "templates"), trim_blocks=True, lstrip_blocks=True)
        self._env.filters["is_in"] = is_in

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
        return template.render(**self._requirements.to_dict())

    @staticmethod
    def _load_memory_requirements() -> UserRequirements:
        with open("user_requirements.yml") as file:
            requirements = yaml.safe_load(file)
        return UserRequirements(**requirements)
