from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


class UnknownNodeTypeError(ApplicationError):
    def __init__(self, node_type: str) -> None:
        message = f"Unknown node type: {node_type}"
        super().__init__(message=message, error_type=ErrorTypes.GENERATOR.value)
