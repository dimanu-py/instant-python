from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class InvalidBuiltInFeaturesValues(ApplicationError):
    def __init__(self, values: list[str], supported_values: list[str]) -> None:
        message = (
            f"Features {', '.join(values)} are not supported. Supported features are: {', '.join(supported_values)}."
        )
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
