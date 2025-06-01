from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class ConfigurationFileNotFound(ApplicationError):
    def __init__(self, path: str) -> None:
        self._message = f"Configuration file not found at '{path}'."
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
