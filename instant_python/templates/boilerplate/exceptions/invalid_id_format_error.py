{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.domain_error import DomainError
{% else %}
from {{ general.source_name }}.errors.domain_error import DomainError
{% endif %}


class InvalidIdFormatError(DomainError):
    def __init__(self) -> None:
        super().__init__(message="User id must be a valid UUID", error_type="invalid_id_format",)
