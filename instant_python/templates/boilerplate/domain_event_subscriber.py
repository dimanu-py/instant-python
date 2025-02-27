from abc import ABC, abstractmethod

from {{ source_name }}.shared.domain.event.domain_event import DomainEvent


class DomainEventSubscriber[EventType: DomainEvent](ABC):
    @staticmethod
    @abstractmethod
    def subscribed_to() -> list[type[EventType]]:
        raise NotImplementedError

    @abstractmethod
    def on(self, event: EventType) -> None:
        raise NotImplementedError
