{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

{% if template_infra_import %}
from {{ general.source_name }}.{{ template_infra_import }}.persistence.sqlalchemy.postgres_settings import PostgresSettings
{% else %}
from {{ general.source_name }}.persistence.sqlalchemy.postgres_settings import PostgresSettings
{% endif %}


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