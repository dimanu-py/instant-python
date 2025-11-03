from expects import be_none, expect, be_empty, be_false

from instant_python.initialize.domain.nodes import File
from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment
from instant_python.initialize.infra.renderer.jinja_project_renderer import JinjaProjectRenderer
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
            (node for node in project_structure.flatten() if isinstance(node, File)), None
        )
        expect(first_file).to_not(be_none)
        expect(first_file.is_empty()).to(be_false)
