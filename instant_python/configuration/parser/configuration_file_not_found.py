from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class ConfigurationFileNotFound(ApplicationError):
    def __init__(self, path: str) -> None:
        message = f"Configuration file not found at '{path}'."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
