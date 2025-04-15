from instant_python.errors.application_error import ApplicationError


class CommandExecutionError(ApplicationError):
    def __init__(self, exit_code: int, stderr_output=None):
        self._message = (
            f"Unexpected error when executing a command, exit code {exit_code}"
        )
        if stderr_output:
            self._message += f": {stderr_output.decode('utf-8').strip()}"
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return "installer_error"

    @property
    def message(self) -> str:
        return self._message
