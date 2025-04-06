{% set template_domain_import = "shared.domain"|compute_base_path(template) %}

from {{ source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent


class AggregateRoot:
    _domain_events: list[DomainEvent]

    def __init__(self) -> None:
        self._domain_events = []

    def record(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def pull_domain_events(self) -> list[DomainEvent]:
        recorded_domain_events = self._domain_events
        self._domain_events = []

        return recorded_domain_events
