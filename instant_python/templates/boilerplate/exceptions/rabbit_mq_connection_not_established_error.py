{% set template_domain_import = "shared.domain"|compute_base_path(template) %}
from {{ source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError


class RabbitMqConnectionNotEstablishedError(DomainError):
	def __init__(self) -> None:
		self._message = "RabbitMQ connection not established."
		self._type = "rabbit_mq_connection"
		super().__init__(self._message)

	@property
	def type(self) -> str:
		return self._type

	@property
	def message(self) -> str:
		return self._message