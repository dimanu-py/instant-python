{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
from collections.abc import AsyncGenerator
import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from {{ general.source_name }}.{{ template_infra_import }}.persistence.sqlalchemy.postgres_settings import PostgresSettings


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