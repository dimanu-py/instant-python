from pathlib import Path

from expects import expect, equal

from instant_python.builder.jinja_environment import JinjaEnvironment
from instant_python.builder.jinja_project_render import JinjaProjectRender
from instant_python.configuration.parser.parser import Parser


class TestJinjaProjectRender:
    def setup_method(self) -> None:
        jinja_environment = JinjaEnvironment(package_name="test", template_directory="builder/resources")
        self._project_render = JinjaProjectRender(jinja_environment=jinja_environment)

    def test_should_render_template_with_project_structure(self) -> None:
        configuration = Parser.parse(str(Path(__file__).parent / "resources" / "config.yml"))

        rendered_project = self._project_render.render_project_structure(context_config=configuration)

        expected_project = {
            "root": [
                {
                    "name": "src",
                    "type": "directory",
                    "python": True,
                    "children": [
                        {
                            "name": "domain",
                            "type": "directory",
                            "python": True,
                            "children": [
                                {
                                    "name": "exceptions",
                                    "type": "directory",
                                    "python": True,
                                    "children": [{"name": "exceptions/domain_error", "type": "boilerplate_file", "extension": ".py"}],
                                }
                            ],
                        },
                        {"name": "application", "type": "directory", "python": True},
                    ],
                },
            ]
        }
        expect(rendered_project).to(equal(expected_project))
