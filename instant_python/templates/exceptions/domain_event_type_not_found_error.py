from {{ general.source_name }}{{ "shared.domain.errors.domain_error" | resolve_import_path(template.name) }} import DomainError


class DomainEventTypeNotFoundError(DomainError):
	def __init__(self, name: str) -> None:
		super().__init__(message=f"Event type {name} not found among subscriber.")
