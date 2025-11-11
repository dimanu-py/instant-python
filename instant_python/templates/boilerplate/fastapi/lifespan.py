from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from {{ general.source_name }}{{ "shared.infra.alembic_migrator" | resolve_import_path(template.name) }} import AlembicMigrator


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
	migrator = AlembicMigrator()
	await migrator.migrate()
	yield