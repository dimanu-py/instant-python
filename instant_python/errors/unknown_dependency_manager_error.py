from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class UnknownDependencyManagerError(ApplicationError):
    def __init__(self, manager: str) -> None:
        self._message = f"Unknown dependency manager: {manager}. Please use 'pdm' or 'uv'."
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.INSTALLER.value

    @property
    def message(self) -> str:
        return self._message
