{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.domain_error import DomainError
{% else %}
from {{ general.source_name }}.errors.domain_error import DomainError
{% endif %}


class RequiredValueError(DomainError):
    def __init__(self) -> None:
        super().__init__(message="Value is required, can't be None", error_type="required_value",)
