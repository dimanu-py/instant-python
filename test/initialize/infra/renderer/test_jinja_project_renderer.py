from expects import be_none, expect, be_empty

from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment
from instant_python.initialize.infra.renderer.jinja_project_renderer import JinjaProjectRenderer
from test.config.domain.mothers.config_schema_mother import ConfigSchemaMother
from test.initialize.utils import test_resources_path


class TestJinjaProjectRenderer:
    def test_should_render_clean_architecture_project_structure(self) -> None:
        config = ConfigSchemaMother.any()
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(test_resources_path())))

        project_structure = renderer.render(context_config=config)

        expect(project_structure).to_not(be_none)
        expect(project_structure).to_not(be_empty)
