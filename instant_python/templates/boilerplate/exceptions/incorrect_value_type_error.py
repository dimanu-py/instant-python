{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from typing import TypeVar

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.domain_error import DomainError
{% else %}
from {{ general.source_name }}.errors.domain_error import DomainError
{% endif %}

T = TypeVar("T")


class IncorrectValueTypeError(DomainError):
    def __init__(self, value: T) -> None:
        super().__init__(message=f"Value '{value}' is not of type {type(value).__name__}", error_type="incorrect_value_type", )
