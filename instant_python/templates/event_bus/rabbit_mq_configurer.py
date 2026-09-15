from {{ general.source_name }}{{ "shared.domain.event.domain_event" | resolve_import_path(template.name) }} import DomainEvent
from {{ general.source_name }}{{ "shared.domain.event.domain_event_subscriber" | resolve_import_path(template.name) }} import (
    DomainEventSubscriber,
)
from {{ general.source_name }}{{ "shared.infra.event.rabbit_mq.rabbit_mq_connection" | resolve_import_path(template.name) }} import (
    RabbitMqConnection,
)
from {{ general.source_name }}{{ "shared.infra.event.rabbit_mq.rabbit_mq_queue_formatter" | resolve_import_path(template.name) }} import (
    RabbitMqQueueFormatter,
)


class RabbitMqConfigurer:
    _queue_formatter: RabbitMqQueueFormatter
    _connection: RabbitMqConnection

    def __init__(self, connection: RabbitMqConnection, queue_formatter: RabbitMqQueueFormatter) -> None:
        self._queue_formatter = queue_formatter
        self._connection = connection

    def configure(self, exchange_name: str, subscribers: list[DomainEventSubscriber[DomainEvent]]) -> None:
        self._create_exchange(exchange_name)
        for subscriber in subscribers:
            self._create_and_bind_queue(subscriber, exchange_name)

    def _create_exchange(self, exchange_name: str) -> None:
        self._connection.create_exchange(name=exchange_name)

    def _create_and_bind_queue(self, subscriber: DomainEventSubscriber[DomainEvent], exchange_name: str) -> None:
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
