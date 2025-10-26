from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class ConfigKeyNotPresent(ApplicationError):
    def __init__(self, missing_keys: list[str], required_keys: list[str]) -> None:
        super().__init__(
            message=f"The following required keys are missing from the config file: {', '.join(missing_keys)}. Required keys are: {', '.join(required_keys)}.",
            error_type=ErrorTypes.CONFIGURATION.value,
        )


class EmptyConfigurationNotAllowed(ApplicationError):
    def __init__(self) -> None:
        super().__init__(message="Configuration file cannot be empty.", error_type=ErrorTypes.CONFIGURATION.value)


class MissingMandatoryFields(ApplicationError):
    def __init__(self, missing_field: str, config_section: str) -> None:
        super().__init__(
            message=(
                f"Mandatory field '{missing_field}' is missing in the '{config_section}' section of the config file."
            ),
            error_type=ErrorTypes.CONFIGURATION.value,
        )
