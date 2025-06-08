import json
from pathlib import Path

from expects import expect, equal

from instant_python.builder.jinja_environment import JinjaEnvironment
from instant_python.builder.jinja_project_render import JinjaProjectRender
from instant_python.configuration.parser.parser import Parser


class TestJinjaProjectRender:
    def setup_method(self) -> None:
        jinja_environment = JinjaEnvironment(package_name="test", template_directory="builder")
        self._project_render = JinjaProjectRender(jinja_environment=jinja_environment)
        self._resources_path = str(Path(__file__).parent / "resources")

    def test_should_render_template_for_clean_architecture_project(self) -> None:
        configuration = Parser.parse(f"{self._resources_path}/clean_architecture_config.yml")

        rendered_project = self._project_render.render_project_structure(context_config=configuration, template_base_dir="resources")

        expected_project = self._load_expected_project(f"{self._resources_path}/clean_architecture/expected_project.json")
        expect(rendered_project).to(equal(expected_project))

    def test_should_render_template_for_domain_driven_design_project(self) -> None:
        configuration = Parser.parse(f"{self._resources_path}/domain_driven_design_config.yml")

        rendered_project = self._project_render.render_project_structure(context_config=configuration, template_base_dir="resources")

        expected_project = self._load_expected_project(f"{self._resources_path}/domain_driven_design/expected_project.json")
        expect(rendered_project).to(equal(expected_project))

    def test_should_render_standard_project_with_git_configuration(self) -> None:
        configuration = Parser.parse(f"{self._resources_path}/standard_project_with_git_config.yml")

        rendered_project = self._project_render.render_project_structure(context_config=configuration, template_base_dir="resources")

        expected_project = self._load_expected_project(f"{self._resources_path}/standard_project/expected_project_with_git.json")
        expect(rendered_project).to(equal(expected_project))

    def test_should_render_standard_project_with_specific_dependency(self) -> None:
        configuration = Parser.parse(f"{self._resources_path}/standard_project_with_dependency_config.yml")

        rendered_project = self._project_render.render_project_structure(context_config=configuration, template_base_dir="resources")

        expected_project = self._load_expected_project(f"{self._resources_path}/standard_project/expected_project_with_dependency.json")
        expect(rendered_project).to(equal(expected_project))

    @staticmethod
    def _load_expected_project(path: str) -> dict:
        with open(path, "r") as file:
            return json.load(file)
