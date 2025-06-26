from abc import ABC


class ApplicationError(Exception, ABC):
    def __init__(self, message: str, error_type: str) -> None:
        self._message = message
        self._type = error_type
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return self._type

    @property
    def message(self) -> str:
        return self._message
