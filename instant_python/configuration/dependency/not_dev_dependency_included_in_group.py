from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class NotDevDependencyIncludedInGroup(ApplicationError):
    def __init__(self, dependency_name: str, dependency_group: str) -> None:
        message = f"Dependency '{dependency_name}' has been included in group '{dependency_group}' but it is not a development dependency. Please ensure that only development dependencies are included in groups."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
