{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent
from {{ general.source_name }}.{{ template_domain_import }}.event.event_bus import EventBus
{% else %}
from {{ general.source_name }}.event.domain_event import DomainEvent
from {{ general.source_name }}.event.event_bus import EventBus
{% endif %}
{% if template_infra_import %}
from {{ general.source_name }}.{{ template_infra_import }}.event.domain_event_json_serializer import (
    DomainEventJsonSerializer,
)
from {{ general.source_name }}.{{ template_infra_import }}.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
{% else %}
from {{ general.source_name }}.event.domain_event_json_serializer import (
    DomainEventJsonSerializer,
)
from {{ general.source_name }}.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
{% endif %}


class RabbitMqEventBus(EventBus):
    def __init__(self, client: RabbitMqConnection, exchange_name: str) -> None:
        self._client = client
        self._exchange_name = exchange_name
        self._event_serializer = DomainEventJsonSerializer()

    def publish(self, events: list[DomainEvent]) -> None:
        for event in events:
            self._client.publish(
                content=self._serialize_event(event),
                exchange=self._exchange_name,
                routing_key=event.name(),
            )

    def _serialize_event(self, event: DomainEvent) -> str:
        return self._event_serializer.serialize(event)
