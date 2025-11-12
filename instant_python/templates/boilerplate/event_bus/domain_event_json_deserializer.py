import json

from {{ general.source_name }}{{ "shared.domain.event.domain_event" | resolve_import_path(template.name) }} import DomainEvent
from {{ general.source_name }}{{ "shared.domain.event.domain_event_subscriber" | resolve_import_path(template.name) }} import (
    DomainEventSubscriber,
)
from {{ general.source_name }}{{ "shared.domain.event.domain_event_type_not_found_errorr" | resolve_import_path(template.name) }} import (
    DomainEventTypeNotFoundError,
)


class DomainEventJsonDeserializer:
    _events_mapping: dict[str, type[DomainEvent]]

    def __init__(self, subscriber: DomainEventSubscriber[DomainEvent]) -> None:
        self._events_mapping = {event.name(): event for event in subscriber.subscribed_to()}

    def deserialize(self, body: bytes) -> DomainEvent:
        content = json.loads(body)
        event_class = self._events_mapping.get(content["data"]["type"])

        if not event_class:
            raise DomainEventTypeNotFoundError(content["data"]["type"])

        return event_class(**content["data"]["attributes"])
