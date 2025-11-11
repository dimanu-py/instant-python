import json

from {{ general.source_name }}{{ "shared.domain.event.domain_event" | resolve_import_path(template.name) }} import DomainEvent


class DomainEventJsonSerializer:
    @staticmethod
    def serialize(event: DomainEvent) -> str:
        body = {
            "data": {
                "id": event.id,
                "type": event.name(),
                "attributes": event.to_dict(),
            }
        }
        return json.dumps(body)
