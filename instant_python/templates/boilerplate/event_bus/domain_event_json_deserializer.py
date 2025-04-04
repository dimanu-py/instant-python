import json

from {{ source_name }}.shared.domain.event.domain_event import DomainEvent
from {{ source_name }}.shared.domain.event.domain_event_subscriber import (
    DomainEventSubscriber,
)
from {{ source_name }}.shared.domain.exceptions.domain_event_type_not_found import (
    DomainEventTypeNotFound,
)


class DomainEventJsonDeserializer:
    _events_mapping: dict[str, type[DomainEvent]]

    def __init__(self, subscriber: DomainEventSubscriber[DomainEvent]) -> None:
        self._events_mapping = {
            event.name(): event for event in subscriber.subscribed_to()
        }

    def deserialize(self, body: bytes) -> DomainEvent:
        content = json.loads(body)
        event_class = self._events_mapping.get(content["data"]["type"])

        if not event_class:
            raise DomainEventTypeNotFound(content["data"]["type"])

        return event_class(**content["data"]["attributes"])
