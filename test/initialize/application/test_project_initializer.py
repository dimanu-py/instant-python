from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.initialize.application.project_initializer import ProjectInitializer
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from test.config.domain.mothers.config_schema_mother import ConfigSchemaMother


class TestProjectInitializer:
    def test_should_initialize_project(self) -> None:
        renderer = Mock(ProjectRenderer)
        config = ConfigSchemaMother.any()

        expect_call(renderer).render(config).returns({})

        project_initializer = ProjectInitializer(
            renderer=renderer,
        )
        project_initializer.execute(config=config)

        expect(renderer).to(have_been_satisfied)
