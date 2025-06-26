from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class FileHasNotBeenCreated(ApplicationError):
    def __init__(self, name: str) -> None:
        message = f"File {name} has not been created yet. Please create the file before trying to fill it."
        super().__init__(message=message, error_type=ErrorTypes.GENERATOR.value)
