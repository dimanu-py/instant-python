from expects import expect, be_true, be_none, equal

from instant_python.builder.jinja_environment import JinjaEnvironment


class TestJinjaEnvironment:
    def test_should_initialize_jinja_environment(self) -> None:
        jinja_env = JinjaEnvironment(package_name="test", template_directory="builder/resources")

        expect(jinja_env._env).not_to(be_none)
        expect(jinja_env._env.trim_blocks).to(be_true)
        expect(jinja_env._env.lstrip_blocks).to(be_true)

    def test_should_register_custom_filters(self) -> None:
        jinja_env = JinjaEnvironment(package_name="test", template_directory="builder/resources")

        expect("is_in" in jinja_env._env.filters).to(be_true)
        expect("compute_base_path" in jinja_env._env.filters).to(be_true)

    def test_should_render_template(self) -> None:
        jinja_env = JinjaEnvironment(package_name="test", template_directory="builder/resources")

        rendered_content = jinja_env.render_template("test_template.j2", {"name": "World"})

        expect(rendered_content).to(equal("Hello World!"))
