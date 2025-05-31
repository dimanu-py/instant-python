from instant_python.configuration.general_configuration import SUPPORTED_DEPENDENCY_MANAGERS
from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class InvalidDependencyManagerValue(ApplicationError):
    def __init__(self, value: str) -> None:
        self._message = f"Invalid dependency manager: {value}. Allowed values are {SUPPORTED_DEPENDENCY_MANAGERS}."
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
