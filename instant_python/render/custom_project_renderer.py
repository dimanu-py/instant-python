from pathlib import Path

import yaml

from instant_python.render.template_file_not_found_error import TemplateFileNotFoundError


class CustomProjectRenderer:
    def __init__(self, template_path: str) -> None:
        self._template_path = Path(template_path).expanduser().resolve()

    def render_project_structure(self) -> dict[str, str]:
        if not self._template_path.is_file():
            raise TemplateFileNotFoundError(self._template_path)
        with open(self._template_path, "r", encoding="utf-8") as f:
            project_structure = yaml.safe_load(f)
            project_structure.append({"name": "pyproject", "type": "boilerplate_file", "extension": ".toml"})
            return project_structure
