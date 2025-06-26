from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class UnknownTemplateError(ApplicationError):
    def __init__(self, template_name: str) -> None:
        message = f"Unknown template type: {template_name}"
        super().__init__(message=message, error_type=ErrorTypes.GENERATOR.value)
