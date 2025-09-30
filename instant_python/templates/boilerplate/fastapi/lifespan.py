{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

{% if template_infra_import %}
from {{ general.source_name }}.{{ template_infra_import }}.alembic_migrator import AlembicMigrator
{% else %}
from {{ general.source_name }}.alembic_migrator import AlembicMigrator
{% endif %}


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
	migrator = AlembicMigrator()
	await migrator.migrate()
	yield