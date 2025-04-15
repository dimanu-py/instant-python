from instant_python.errors.application_error import ApplicationError


class UnknownDependencyManagerError(ApplicationError):
    def __init__(self, manager: str) -> None:
        self._message = (
            f"Unknown dependency manager: {manager}. Please use 'pdm' or 'uv'."
        )
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return "installer_error"

    @property
    def message(self) -> str:
        return self._message
