from abc import ABC, abstractmethod

from {{ source_name }}.shared.domain.event.domain_event import DomainEvent


class EventBus(ABC):
    @abstractmethod
    def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError
