{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from abc import ABC, abstractmethod

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent
{% else %}
from {{ general.source_name }}.event.domain_event import DomainEvent
{% endif %}


class EventBus(ABC):
    @abstractmethod
    async def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError
