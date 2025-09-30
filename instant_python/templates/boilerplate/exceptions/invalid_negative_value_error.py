{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.domain_error import DomainError
{% else %}
from {{ general.source_name }}.errors.domain_error import DomainError
{% endif %}


class InvalidNegativeValueError(DomainError):
    def __init__(self, value: int) -> None:
        super().__init__(message=f"Invalid negative value: {value}", error_type="invalid_negative_value",)
