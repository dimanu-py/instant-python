from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class MissingMandatoryFields(ApplicationError):
    def __init__(self, missing_field: str, config_section: str) -> None:
        super().__init__(
            message=(
                f"Mandatory field '{missing_field}' is missing in the '{config_section}' section of the config file."
            ),
            error_type=ErrorTypes.CONFIGURATION.value,
        )
