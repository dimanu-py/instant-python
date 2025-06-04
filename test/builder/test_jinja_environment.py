from expects import expect, be_true, be_none

from instant_python.builder.jinja_environment import JinjaEnvironment


class TestJinjaEnvironment:
    def test_should_initialize_jinja_environment(self) -> None:
        jinja_env = JinjaEnvironment()

        expect(jinja_env._env).not_to(be_none)
        expect(jinja_env._env.trim_blocks).to(be_true)
        expect(jinja_env._env.lstrip_blocks).to(be_true)

    def test_should_register_custom_filters(self) -> None:
        jinja_env = JinjaEnvironment()

        expect("is_in" in jinja_env._env.filters).to(be_true)
        expect("compute_base_path" in jinja_env._env.filters).to(be_true)
