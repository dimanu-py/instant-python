from sindripy.value_objects import Aggregate
from {{ general.source_name }}{{ "shared.domain.event.domain_event" | resolve_import_path(template.name) }} import DomainEvent


class EventAggregate(Aggregate):
    _domain_events: list[DomainEvent]

    def __init__(self) -> None:
        super().__init__()
        self._domain_events = []

    def record(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def pull_domain_events(self) -> list[DomainEvent]:
        recorded_domain_events = self._domain_events
        self._domain_events = []

        return recorded_domain_events
