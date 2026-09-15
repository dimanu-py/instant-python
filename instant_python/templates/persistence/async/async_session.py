from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from {{ general.source_name }}{{ "shared.infra.persistence.postgres_settings" | resolve_import_path(template.name) }} import PostgresSettings


settings = PostgresSettings()  # type: ignore
engine = create_async_engine(str(settings.postgres_url))


async def get_async_session() -> AsyncGenerator[AsyncSession]:
    async with AsyncSession(engine) as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise