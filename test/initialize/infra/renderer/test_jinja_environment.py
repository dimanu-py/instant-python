from expects import be_none, expect, have_keys, equal, raise_error
from jinja2 import TemplateNotFound

from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment
from test.initialize.utils import resources_path


class TestJinjaEnvironment:
    def setup_method(self) -> None:
        self._jinja_environment = JinjaEnvironment(user_template_path=str(resources_path()))

    def test_should_initialize_environment(self) -> None:
        expect(self._jinja_environment._env).not_to(be_none)

    def test_should_register_custom_filters(self) -> None:
        self._jinja_environment.add_filter("custom_filter", lambda x: x)

        expect(self._jinja_environment._env.filters).to(have_keys("custom_filter"))

    def test_should_render_template_from_user_templates_folder_when_template_is_found(self) -> None:
        rendered_content = self._jinja_environment.render_template("hello_world.j2", {"name": "World"})

        expect(rendered_content).to(equal("Hello World!"))

    def test_should_render_template_from_default_templates_folder_when_custom_template_is_not_found(self) -> None:
        rendered_content = self._jinja_environment.render_template(".gitignore")

        expect(rendered_content).to_not(be_none)

    def test_should_raise_error_when_template_is_not_found_anywhere(self) -> None:
        expect(lambda: self._jinja_environment.render_template("non_existing_template.j2")).to(
            raise_error(TemplateNotFound)
        )
