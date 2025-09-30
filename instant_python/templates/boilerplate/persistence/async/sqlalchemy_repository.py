{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
from typing import TypeVar

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.uuid import Uuid
{% else %}
from {{ general.source_name }}.value_objects.uuid import Uuid
{% endif %}
{% if template_infra_import %}
from {{ general.source_name }}.{{ template_infra_import }}.persistence.sqlalchemy.base import Base
{% else %}
from {{ general.source_name }}.persistence.sqlalchemy.base import Base
{% endif %}
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker


Entity = TypeVar("Entity")


class SqlalchemyRepository[Model: Base]:
	_model_class: type[Model]
	_session_maker: async_sessionmaker[AssyncSession]

	def __init__(self, engine: AsyncEngine, model_class: type[Model]) -> None:
		self._session_maker = async_sessionmaker(bind=engine)
		self._model_class = model_class

	async def persist(self, entity: Entity) -> None:
		async with self._session_maker() as session:
			entity_model = self._model_class(**entity.to_dict())
			session.add(entity_model)
			await session.commit()

	async def find(self, entity_id: Uuid) -> Entity:
		async with self._session_maker() as session:
			entity_model = await session.get(self._model_class, entity_id.value)
			return entity_model.to_aggregate() if entity_model else None
