{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from unittest.mock import AsyncMock

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.event.domain_event import DomainEvent
from {{ general.source_name }}.{{ template_domain_import }}.event.event_bus import EventBus
{% else %}
from {{ general.source_name }}.event.domain_event import DomainEvent
from {{ general.source_name }}.event.event_bus import EventBus
{% endif %}


class MockEventBus(EventBus):

	def __init__(self) -> None:
		self._mock_publish = AsyncMock()

	async def publish(self, events: list[DomainEvent]) -> None:
		await self._mock_publish(events)

	def should_have_published(self, event: DomainEvent) -> None:
		self._mock_publish.assert_awaited_once_with([event])
		self._mock_publish.reset_mock()