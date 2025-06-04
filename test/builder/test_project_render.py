import pytest
from expects import expect, equal

from instant_python.builder.jinja_environment import JinjaEnvironment
from instant_python.builder.project_render import ProjectRender


class TestProjectRender:
    @pytest.mark.xfail(reason="This test is not implemented yet")
    def test_should_render_folder_structure(self) -> None:
        render = ProjectRender(jinja_environment=JinjaEnvironment(package_name="test", template_directory="builder/resources"))

        project_structure = render.process_project(configuration=config)

        expected_project_structure = {}
        expect(project_structure).to(equal(expected_project_structure))
