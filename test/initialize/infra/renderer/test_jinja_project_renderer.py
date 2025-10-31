from expects import be_none, expect, be_empty

from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment
from instant_python.initialize.infra.renderer.jinja_project_renderer import JinjaProjectRenderer
from instant_python.project_creator.node import NodeType
from instant_python.shared.supported_templates import SupportedTemplates
from test.config.domain.mothers.config_schema_mother import ConfigSchemaMother
from test.initialize.utils import resources_path


class TestJinjaProjectRenderer:
    def test_should_render_standard_project_structure(self) -> None:
        config = ConfigSchemaMother.with_template(template=SupportedTemplates.STANDARD.value)
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(resources_path())))

        project_structure = renderer.render(context_config=config)

        expect(project_structure).to_not(be_none)
        expect(project_structure).to_not(be_empty)

    def test_should_include_file_template_content_in_project_structure(self) -> None:
        config = ConfigSchemaMother.with_template(template=SupportedTemplates.STANDARD.value)
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(resources_path())))

        project_structure = renderer.render(context_config=config)

        first_file = next(
            (item for item in self._flatten_structure(project_structure) if item.get("type") == "file"), None
        )
        expect(first_file).to_not(be_none)
        expect(first_file.get("content")).to_not(be_empty)

    def _flatten_structure(self, structure):
        for item in structure:
            yield item
            if item.get("type") == NodeType.DIRECTORY:
                yield from self._flatten_structure(item.get("children", []))
