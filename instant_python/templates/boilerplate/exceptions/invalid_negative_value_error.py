from {{ general.source_name }}{{ "shared.domain.errors.domain_error" | resolve_import_path(template.name) }} import DomainError


class InvalidNegativeValueError(DomainError):
    def __init__(self, value: int) -> None:
        super().__init__(message=f"Invalid negative value: {value}")
