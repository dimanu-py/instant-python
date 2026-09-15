from {{ general.source_name }}{{ "shared.domain.errors.domain_error" | resolve_import_path(template.name) }} import DomainError



class RabbitMqConnectionNotEstablishedError(DomainError):
    def __init__(self) -> None:
        super().__init__(message="RabbitMQ connection not established.")
