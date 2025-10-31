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
