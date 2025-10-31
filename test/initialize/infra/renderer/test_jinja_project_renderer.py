from expects import be_none, expect, be_empty

from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment
from instant_python.initialize.infra.renderer.jinja_project_renderer import JinjaProjectRenderer
from instant_python.shared.supported_templates import SupportedTemplates
from test.config.domain.mothers.config_schema_mother import ConfigSchemaMother
from test.initialize.utils import test_resources_path


class TestJinjaProjectRenderer:
    def test_should_render_standard_project_structure(self) -> None:
        config = ConfigSchemaMother.with_template(
            template=SupportedTemplates.STANDARD.value
        )
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(test_resources_path())))

        project_structure = renderer.render(context_config=config)

        expect(project_structure).to_not(be_none)
        expect(project_structure).to_not(be_empty)

    def test_should_include_file_template_content_in_project_structure(self) -> None:
        config = ConfigSchemaMother.with_template(
            template=SupportedTemplates.STANDARD.value
        )
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(test_resources_path())))

        project_structure = renderer.render(context_config=config)

        first_file = self._extract_first_file_from_structure(project_structure)
        expect(first_file).to_not(be_none)
        expect(first_file.get("content")).to_not(be_empty)

    def _extract_first_file_from_structure(self, project_structure):
        for item in project_structure:
            if item.get("type") == "file":
                return item
            elif item.get("type") == "directory":
                nested_file = self._extract_first_file_from_structure(item.get("children", []))
                if nested_file:
                    return nested_file
        return None