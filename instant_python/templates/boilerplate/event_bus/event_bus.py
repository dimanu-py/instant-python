{% set template_domain_import = "shared.domain"|compute_base_path(template) %}
from abc import ABC, abstractmethod

from {{ source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent


class EventBus(ABC):
    @abstractmethod
    async def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError
