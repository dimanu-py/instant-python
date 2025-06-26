from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class GitUserOrEmailNotPresent(ApplicationError):
    def __init__(self) -> None:
        message = "When initializing a git repository, both username and email must be provided."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
