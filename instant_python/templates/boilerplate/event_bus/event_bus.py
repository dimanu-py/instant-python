from abc import ABC, abstractmethod

from {{ general.source_name }}{{ "shared.domain.event.domain_event" | resolve_import_path(template.name) }} import DomainEvent


class EventBus(ABC):
    @abstractmethod
    async def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError
