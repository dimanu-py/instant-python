import json
from pathlib import Path

from approvaltests import verify

from instant_python.render.custom_project_renderer import CustomProjectRenderer


class TestCustomProjectRenderer:
    def setup_method(self) -> None:
        template_path = Path(__file__).parent / "resources" / "custom_template.yml"
        self._project_renderer = CustomProjectRenderer(template_path=str(template_path))

    def test_should_render_custom_template(self) -> None:
        rendered_project = self._project_renderer.render_project_structure()

        rendered_project_json = json.dumps(rendered_project, indent=2, sort_keys=True)
        verify(rendered_project_json)
