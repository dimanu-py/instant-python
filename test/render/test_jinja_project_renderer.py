import json
from pathlib import Path

import pytest
from approvaltests import verify
from approvaltests.namer import NamerFactory

from instant_python.render.jinja_environment import JinjaEnvironment
from instant_python.render.jinja_project_renderer import JinjaProjectRenderer
from instant_python.configuration.parser.parser import Parser


class TestJinjaProjectRenderer:
    def setup_method(self) -> None:
        jinja_environment = JinjaEnvironment(package_name="test", template_directory="render")
        self._project_renderer = JinjaProjectRenderer(jinja_environment=jinja_environment)

    @pytest.mark.parametrize(
        "config_path",
        [
            pytest.param("clean_architecture_config.yml", id="clean_architecture"),
            pytest.param("domain_driven_design_config.yml", id="domain_driven_design"),
            pytest.param("standard_project_with_git_config.yml", id="standard_project_with_git"),
            pytest.param("standard_project_with_dependency_config.yml", id="standard_project_with_dependency"),
        ],
    )
    def test_should_render_template_for(self, config_path: str) -> None:
        resources_path = str(Path(__file__).parent / "resources")
        configuration = Parser.parse_from_file(f"{resources_path}/{config_path}")

        rendered_project = self._project_renderer.render_project_structure(
            context_config=configuration, template_base_dir="resources"
        )

        rendered_project_json = json.dumps(rendered_project, indent=2, sort_keys=True)
        verify(rendered_project_json, options=NamerFactory.with_parameters(config_path))
