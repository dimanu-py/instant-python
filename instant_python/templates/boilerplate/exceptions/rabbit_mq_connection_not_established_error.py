{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from {{ general.source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError


class RabbitMqConnectionNotEstablishedError(DomainError):
	def __init__(self) -> None:
		self._message = "RabbitMQ connection not established."
		self._type = "rabbit_mq_connection"
		super().__init__(message=self._message, error_type=self._type)
