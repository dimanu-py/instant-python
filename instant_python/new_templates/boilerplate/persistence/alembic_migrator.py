{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
import asyncio

from {{ general.source_name }}.{{ template_infra_import }}.persistence.sqlalchemy.postgres_settings import PostgresSettings
from alembic import command
from alembic.config import Config


class AlembicMigrator:
	def __init__(self) -> None:
		self._settings = PostgresSettings()  # type: ignore
		self._alembic_config = Config()

	async def migrate(self) -> None:
		self._alembic_config.set_main_option(
			"sqlalchemy.url", self._settings.postgres_url
		)
		self._alembic_config.set_main_option("script_location", "migrations")
		loop = asyncio.get_event_loop()
		await loop.run_in_executor(None, command.upgrade, self._alembic_config, "head")  # type: ignore