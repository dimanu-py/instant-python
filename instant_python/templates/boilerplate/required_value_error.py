from {{ source_name }}.shared.domain.exceptions.domain_error import DomainError


class RequiredValueError(DomainError):
    def __init__(self) -> None:
        self._message = "Value is required, can't be None"
        self._type = "required_value"
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return self._type

    @property
    def message(self) -> str:
        return self._message
