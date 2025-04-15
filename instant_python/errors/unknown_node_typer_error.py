from instant_python.errors.application_error import ApplicationError
from instant_python.errors.error_types import ErrorTypes


class UnknownNodeTypeError(ApplicationError):
    def __init__(self, node_type: str) -> None:
        self._message = f"Unknown node type: {node_type}"
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return ErrorTypes.GENERATOR.value

    @property
    def message(self) -> str:
        return self._message
