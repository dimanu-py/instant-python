{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.domain_error import DomainError
{% else %}
from {{ general.source_name }}.errors.domain_error import DomainError
{% endif %}

class DomainEventTypeNotFoundError(DomainError):
	def __init__(self, name: str) -> None:
		super().__init__(message=f"Event type {name} not found among subscriber.", error_type="domain_event_type_not_found",)
