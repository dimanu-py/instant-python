{% set template_infra_import = "shared.infra"|compute_base_path(template) %}
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from {{ source_name }}.{{ template_infra_import }}.alembic_migrator import AlembicMigrator


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
	migrator = AlembicMigrator()
	await migrator.migrate()
	yield