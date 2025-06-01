from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class BoundedContextNotApplicable(ApplicationError):
    def __init__(self, value: str) -> None:
        self._message = (
            f"Bounded context feature is not applicable for template '{value}'. Is only applicable for 'domain_driven_design' template."
        )
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
