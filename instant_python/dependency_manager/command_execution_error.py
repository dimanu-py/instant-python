from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class CommandExecutionError(ApplicationError):
    def __init__(self, exit_code: int, stderr_output: str = None) -> None:
        message = f"Unexpected error when executing a command, exit code {exit_code}"
        if stderr_output:
            message += f": {stderr_output.decode('utf-8').strip()}"
        super().__init__(message=message, error_type=ErrorTypes.INSTALLER.value)
