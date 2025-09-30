{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
import json

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event_subscriber import (
    DomainEventSubscriber,
)
from {{ general.source_name }}.{{ template_domain_import }}.errors.domain_event_type_not_found_error import (
    DomainEventTypeNotFoundError,
)
{% else %}
from {{ general.source_name }}.event.domain_event import DomainEvent
from {{ general.source_name }}.event.domain_event_subscriber import (
    DomainEventSubscriber,
)
from {{ general.source_name }}.errors.domain_event_type_not_found_error import (
    DomainEventTypeNotFoundError,
)
{% endif %}


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
            raise DomainEventTypeNotFoundError(content["data"]["type"])

        return event_class(**content["data"]["attributes"])
