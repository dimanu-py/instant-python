from expects import be_none, expect

from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment


class TestJinjaEnvironment:
    def test_should_initialize_environment(self) -> None:
        jinja_environment = JinjaEnvironment()

        expect(jinja_environment._env).not_to(be_none)
