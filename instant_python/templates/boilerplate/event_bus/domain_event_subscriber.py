{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if pythono_version in ["3.12", "3.13"] %}
from abc import ABC, abstractmethod

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent
{% else %}
from {{ general.source_name }}.event.domain_event import DomainEvent
{% endif %}


class DomainEventSubscriber[EventType: DomainEvent](ABC):
    @staticmethod
    @abstractmethod
    def subscribed_to() -> list[type[EventType]]:
        raise NotImplementedError

    @abstractmethod
    def on(self, event: EventType) -> None:
        raise NotImplementedError
{% else %}
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent
{% else %}
from {{ general.source_name }}.event.domain_event import DomainEvent
{% endif %}

EventType = TypeVar("EventType", bound=DomainEvent)

class DomainEventSubscriber(Generic[EventType], ABC):
    @staticmethod
    @abstractmethod
    def subscribed_to() -> list[type[EventType]]:
        raise NotImplementedError

    @abstractmethod
    def on(self, event: EventType) -> None:
        raise NotImplementedError
{% endif %}
