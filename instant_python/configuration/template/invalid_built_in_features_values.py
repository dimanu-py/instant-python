from instant_python.configuration.template.constants import SUPPORTED_BUILT_IN_FEATURES
from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class InvalidBuiltInFeaturesValues(ApplicationError):
    def __init__(self, values: list[str]) -> None:
        self._message = f"Features {', '.join(values)} are not supported. Supported features are: {', '.join(SUPPORTED_BUILT_IN_FEATURES)}."
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.CONFIGURATION.value

    @property
    def message(self) -> str:
        return self._message
