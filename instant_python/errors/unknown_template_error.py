from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class UnknownTemplateError(ApplicationError):
    def __init__(self, template_name: str) -> None:
        self._message = f"Uknown template type: {template_name}"
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.GENERATOR.value

    @property
    def message(self) -> str:
        return self._message
