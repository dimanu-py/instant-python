from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class EmptyConfigurationNotAllowed(ApplicationError):
    def __init__(self) -> None:
        message = "Configuration file cannot be empty."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
