from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class InvalidPythonVersionValue(ApplicationError):
    def __init__(self, value: str, supported_values: list[str]) -> None:
        message = f"Invalid Python version: {value}. Allowed versions are {', '.join(supported_values)}."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
