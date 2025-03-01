from {{ source_name }}.shared.domain.exceptions.domain_error import DomainError


class DomainEventTypeNotFound(DomainError):
	def __init__(self, name: str) -> None:
		self._message = f"Event type {name} not found among subscriber."
		self._type = "domain_event_type_not_found"
		super().__init__(self._message)

	@property
	def type(self) -> str:
		return self._type

	@property
	def message(self) -> str:
		return self._message
