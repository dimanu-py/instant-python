from pathlib import Path

import yaml

from instant_python.errors.template_file_not_found_error import (
    TemplateFileNotFoundError,
)
from instant_python.project_generator.template_manager import TemplateManager


class CustomTemplateManager(TemplateManager):
    def __init__(self, template_path: str) -> None:
        self._template_path = Path(template_path).expanduser().resolve()

    def get_project(self, template_name: str) -> dict[str, str]:
        if not self._template_path.is_file():
            raise TemplateFileNotFoundError(self._template_path)
        with open(self._template_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
