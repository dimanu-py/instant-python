from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class BoundedContextNotApplicable(ApplicationError):
    def __init__(self, value: str) -> None:
        message = f"Bounded context feature is not applicable for template '{value}'. Is only applicable for 'domain_driven_design' template."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
