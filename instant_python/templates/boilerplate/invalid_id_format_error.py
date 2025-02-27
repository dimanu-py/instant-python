from {{ source_name }}.shared.domain.exceptions.domain_error import DomainError


class InvalidIdFormatError(DomainError):
	def __init__(self) -> None:
		self._message = "User id must be a valid UUID"
		self._type = "invalid_id_format"
		super().__init__(self._message)

	@property
	def type(self) -> str:
		return self._type

	@property
	def message(self) -> str:
		return self._message