from collections.abc import AsyncGenerator
import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from {{ general.source_name }}{{ "shared.infra.persistence.postgres_settings" | resolve_import_path(template.name) }} import PostgresSettings


@pytest.fixture
async def engine() -> AsyncGenerator[AsyncEngine]:
	settings = PostgresSettings()  # type: ignore
	engine = create_async_engine(settings.postgres_url)

	async with engine.begin() as conn:
		await conn.run_sync(EntityModel.metadata.create_all)

	yield engine

	async with engine.begin() as conn:
		await conn.run_sync(EntityModel.metadata.drop_all)
	await engine.dispose()