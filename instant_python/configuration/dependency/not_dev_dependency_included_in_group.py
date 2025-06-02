from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class NotDevDependencyIncludedInGroup(ApplicationError):
    def __init__(self, dependency_name: str, dependency_group: str) -> None:
        self._message = f"Dependency '{dependency_name}' has been included in group '{dependency_group}' but it is not a development dependency. Please ensure that only development dependencies are included in groups."
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
