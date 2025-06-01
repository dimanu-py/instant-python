from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class MissingMandatoryFields(ApplicationError):
    def __init__(self, missing_field: str, config_section: str) -> None:
        self._message = f"Mandatory field '{missing_field}' is missing in the '{config_section}' section of the configuration file."
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
