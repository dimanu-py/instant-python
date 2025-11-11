from typing import TypeVar

from {{ general.source_name }}{{ "shared.domain.errors.domain_error" | resolve_import_path(template.name) }} import DomainError

T = TypeVar("T")


class IncorrectValueTypeError(DomainError):
    def __init__(self, value: T) -> None:
        super().__init__(message=f"Value '{value}' is not of type {type(value).__name__}")
