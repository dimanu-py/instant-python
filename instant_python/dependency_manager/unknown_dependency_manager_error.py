from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class UnknownDependencyManagerError(ApplicationError):
    def __init__(self, manager: str) -> None:
        message = f"Unknown dependency manager: {manager}. Please use 'pdm' or 'uv'."
        super().__init__(message=message, error_type=ErrorTypes.INSTALLER.value)
