{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from {{ general.source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError


class InvalidNegativeValueError(DomainError):
    def __init__(self, value: int) -> None:
        self._message = f"Invalid negative value: {value}"
        self._type = "invalid_negative_value"
        super().__init__(message=self._message, error_type=self._type)
