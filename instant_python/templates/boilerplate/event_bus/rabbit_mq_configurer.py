{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event_subscriber import (
    DomainEventSubscriber,
)
{% else %}
from {{ general.source_name }}.event.domain_event import DomainEvent
from {{ general.source_name }}.event.domain_event_subscriber import (
    DomainEventSubscriber,
)
{% endif %}
{% if template_infra_import %}
from {{ general.source_name }}.{{ template_infra_import }}.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
from {{ general.source_name }}.{{ template_infra_import }}.event.rabbit_mq.rabbit_mq_queue_formatter import (
    RabbitMqQueueFormatter,
)
{% else %}
from {{ general.source_name }}.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
from {{ general.source_name }}.event.rabbit_mq.rabbit_mq_queue_formatter import (
    RabbitMqQueueFormatter,
)
{% endif %}


class RabbitMqConfigurer:
    _queue_formatter: RabbitMqQueueFormatter
    _connection: RabbitMqConnection

    def __init__(
        self, connection: RabbitMqConnection, queue_formatter: RabbitMqQueueFormatter
    ) -> None:
        self._queue_formatter = queue_formatter
        self._connection = connection

    def configure(
        self, exchange_name: str, subscribers: list[DomainEventSubscriber[DomainEvent]]
    ) -> None:
        self._create_exchange(exchange_name)
        for subscriber in subscribers:
            self._create_and_bind_queue(subscriber, exchange_name)

    def _create_exchange(self, exchange_name: str) -> None:
        self._connection.create_exchange(name=exchange_name)

    def _create_and_bind_queue(
        self, subscriber: DomainEventSubscriber[DomainEvent], exchange_name: str
    ) -> None:
        routing_keys = self._get_queues_routing_keys_for(subscriber)
        queue_name = self._queue_formatter.format(subscriber)
        self._connection.create_queue(name=queue_name)

        for routing_key in routing_keys:
            self._connection.bind_queue_to_exchange(
                queue_name=queue_name,
                exchange_name=exchange_name,
                routing_key=routing_key,
            )

    @staticmethod
    def _get_queues_routing_keys_for(
        subscriber: DomainEventSubscriber[DomainEvent],
    ) -> list[str]:
        return [event.name() for event in subscriber.subscribed_to()]
