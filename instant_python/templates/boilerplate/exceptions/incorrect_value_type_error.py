{% set template_domain_import = "shared.domain"|compute_base_path(template) %}
from typing import TypeVar

from {{ source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError

T = TypeVar("T")


class IncorrectValueTypeError(DomainError):
    def __init__(self, value: T) -> None:
        self._message = f"Value '{value}' is not of type {type(value).__name__}"
        self._type = "incorrect_value_type"
        super().__init__(self._message)

    @property
    def type(self) -> str:
        return self._type

    @property
    def message(self) -> str:
        return self._message
