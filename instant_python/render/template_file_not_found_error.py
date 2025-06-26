from pathlib import Path

from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class TemplateFileNotFoundError(ApplicationError):
    def __init__(self, template_path: str | Path) -> None:
        message = f"Could not find YAML file at: {template_path}"
        super().__init__(message=message, error_type=ErrorTypes.GENERATOR.value)
