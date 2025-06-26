from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class ConfigKeyNotPresent(ApplicationError):
    def __init__(self, missing_keys: list[str], required_keys: list[str]) -> None:
        message = f"The following required keys are missing from the configuration file: {', '.join(missing_keys)}. Required keys are: {', '.join(required_keys)}."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
