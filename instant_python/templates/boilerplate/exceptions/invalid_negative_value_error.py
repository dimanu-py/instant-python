from {{ source_name }}.shared.domain.exceptions.domain_error import DomainError


class InvalidNegativeValueError(DomainError):
    def __init__(self, value: int) -> None:
        self._message = f"Invalid negative value: {value}"
        self._type = "invalid_negative_value"
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return self._type

    @property
    def message(self) -> str:
        return self._message
