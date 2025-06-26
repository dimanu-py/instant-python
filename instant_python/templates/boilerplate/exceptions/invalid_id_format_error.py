{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from {{ general.source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError


class InvalidIdFormatError(DomainError):
	def __init__(self) -> None:
		self._message = "User id must be a valid UUID"
		self._type = "invalid_id_format"
		super().__init__(message=self._message, error_type=self._type)
