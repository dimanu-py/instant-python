from expects import be_none, expect, have_keys

from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment


class TestJinjaEnvironment:
    def test_should_initialize_environment(self) -> None:
        jinja_environment = JinjaEnvironment()

        expect(jinja_environment._env).not_to(be_none)

    def test_should_register_custom_filters(self) -> None:
        jinja_environment = JinjaEnvironment()

        jinja_environment.add_filter("custom_filter", lambda x: x)

        expect(jinja_environment._env.filters).to(have_keys("custom_filter"))
