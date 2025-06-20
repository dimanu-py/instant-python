{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from {{ general.source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError


class DomainEventTypeNotFoundError(DomainError):
	def __init__(self, name: str) -> None:
		self._message = f"Event type {name} not found among subscriber."
		self._type = "domain_event_type_not_found"
		super().__init__(message=self._message, error_type=self._type)
