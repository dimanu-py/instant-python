from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class BoundedContextNotSpecified(ApplicationError):
    def __init__(self) -> None:
        message = "Option to specify bounded context is set as True, but either bounded context or aggregate name is not specified."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
