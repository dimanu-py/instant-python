from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class InvalidDependencyManagerValue(ApplicationError):
    def __init__(self, value: str, supported_values: list[str]) -> None:
        self._message = f"Invalid dependency manager: {value}. Allowed values are {', '.join(supported_values)}."
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
