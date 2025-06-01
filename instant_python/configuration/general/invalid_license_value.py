from instant_python.configuration.general.constants import SUPPORTED_LICENSES
from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class InvalidLicenseValue(ApplicationError):
    def __init__(self, value: str) -> None:
        self._message = (
            f"Invalid license: {value}. Allowed values are {SUPPORTED_LICENSES}."
        )
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
