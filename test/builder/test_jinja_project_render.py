import json
from pathlib import Path

import pytest
from expects import expect, equal

from instant_python.builder.jinja_environment import JinjaEnvironment
from instant_python.builder.jinja_project_render import JinjaProjectRender
from instant_python.configuration.parser.parser import Parser


class TestJinjaProjectRender:
    def setup_method(self) -> None:
        jinja_environment = JinjaEnvironment(package_name="test", template_directory="builder")
        self._project_render = JinjaProjectRender(jinja_environment=jinja_environment)

    @pytest.mark.parametrize(
        "config_path, expected_path",
        [
            pytest.param("clean_architecture_config.yml", "clean_architecture/expected_project.json", id="clean_architecture"),
            pytest.param("domain_driven_design_config.yml", "domain_driven_design/expected_project.json", id="domain_driven_design"),
            pytest.param(
                "standard_project_with_git_config.yml", "standard_project/expected_project_with_git.json", id="standard_project_with_git"
            ),
            pytest.param(
                "standard_project_with_dependency_config.yml",
                "standard_project/expected_project_with_dependency.json",
                id="standard_project_with_dependency",
            ),
        ],
    )
    def test_should_render_template_for(self, config_path: str, expected_path: str) -> None:
        resources_path = str(Path(__file__).parent / "resources")
        configuration = Parser.parse(f"{resources_path}/{config_path}")

        rendered_project = self._project_render.render_project_structure(context_config=configuration, template_base_dir="resources")

        expected_project = self._load_expected_project(f"{resources_path}/{expected_path}")
        expect(rendered_project).to(equal(expected_project))

    @staticmethod
    def _load_expected_project(path: str) -> dict:
        with open(path, "r") as file:
            return json.load(file)
