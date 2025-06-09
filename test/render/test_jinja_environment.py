from expects import expect, be_true, be_none, equal

from instant_python.render.jinja_environment import JinjaEnvironment


class TestJinjaEnvironment:
    def setup_method(self) -> None:
        self._jinja_environment = JinjaEnvironment(package_name="test", template_directory="render/resources")

    def test_should_initialize_jinja_environment(self) -> None:
        expect(self._jinja_environment._env).not_to(be_none)
        expect(self._jinja_environment._env.trim_blocks).to(be_true)
        expect(self._jinja_environment._env.lstrip_blocks).to(be_true)

    def test_should_register_custom_filters(self) -> None:
        expect("is_in" in self._jinja_environment._env.filters).to(be_true)
        expect("compute_base_path" in self._jinja_environment._env.filters).to(be_true)
        expect("has_dependency" in self._jinja_environment._env.filters).to(be_true)

    def test_should_render_template(self) -> None:
        rendered_content = self._jinja_environment.render_template("test_template.j2", {"name": "World"})

        expect(rendered_content).to(equal("Hello World!"))
