import re

from {{ general.source_name }}{{ "shared.domain.event.domain_event" | resolve_import_path(template.name) }} import DomainEvent
from {{ general.source_name }}{{ "shared.domain.event.domain_event_subscriber" | resolve_import_path(template.name) }} import (
    DomainEventSubscriber,
)


class RabbitMqQueueFormatter:
    _bounded_context: str
    CAMEL_CASE_TO_SNAKE_CASE_PATTERN = r"(?<!^)(?=[A-Z])"

    def __init__(self, bounded_context: str) -> None:
        self._bounded_context = bounded_context

    def format(self, subscriber: DomainEventSubscriber[DomainEvent]) -> str:
        unformatted_subscriber_name = subscriber.__class__.__name__
        formatted_subscriber_name = re.sub(
            self.CAMEL_CASE_TO_SNAKE_CASE_PATTERN, "_", unformatted_subscriber_name
        ).lower()
        return f"{self._bounded_context}.{formatted_subscriber_name}"
