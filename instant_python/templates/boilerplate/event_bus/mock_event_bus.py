from unittest.mock import AsyncMock

from {{ source_name }}.shared.domain.event.domain_event import DomainEvent
from {{ source_name }}.shared.domain.event.event_bus import EventBus


class MockEventBus(EventBus):

	def __init__(self) -> None:
		self._mock_publish = AsyncMock()

	async def publish(self, events: list[DomainEvent]) -> None:
		await self._mock_publish(events)

	def should_have_published(self, event: DomainEvent) -> None:
		self._mock_publish.assert_awaited_once_with([event])
		self._mock_publish.reset_mock()