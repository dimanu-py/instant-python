from pathlib import Path

from expects import be_none, expect, have_keys, equal, raise_error
from jinja2 import TemplateNotFound

from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment


class TestJinjaEnvironment:
    def test_should_initialize_environment(self) -> None:
        jinja_environment = JinjaEnvironment(".")

        expect(jinja_environment._env).not_to(be_none)

    def test_should_register_custom_filters(self) -> None:
        jinja_environment = JinjaEnvironment(".")

        jinja_environment.add_filter("custom_filter", lambda x: x)

        expect(jinja_environment._env.filters).to(have_keys("custom_filter"))

    def test_should_render_template_from_user_templates_folder_when_template_is_found(self) -> None:
        template_path = str(Path(__file__).parent / "resources")
        jinja_environment = JinjaEnvironment(template_path)

        rendered_content = jinja_environment.render_template("hello_world.j2", {"name": "World"})

        expect(rendered_content).to(equal("Hello World!"))

    def test_should_render_template_from_default_templates_folder_when_custom_template_is_not_found(self) -> None:
        jinja_environment = JinjaEnvironment(".")


        expect(rendered_content).to_not(be_none)

    def test_should_raise_error_when_template_is_not_found_anywhere(self) -> None:
        jinja_environment = JinjaEnvironment(".")

        expect(lambda: jinja_environment.render_template("non_existing_template.j2")).to(raise_error(TemplateNotFound))
