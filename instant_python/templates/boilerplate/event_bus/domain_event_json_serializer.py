{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
import json

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent
{% else %}
from {{ general.source_name }}.event.domain_event import DomainEvent
{% endif %}


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
