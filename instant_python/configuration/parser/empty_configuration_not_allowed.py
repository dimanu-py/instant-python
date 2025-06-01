from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class EmptyConfigurationNotAllowed(ApplicationError):
    def __init__(self) -> None:
        self._message = "Configuration file cannot be empty."
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
