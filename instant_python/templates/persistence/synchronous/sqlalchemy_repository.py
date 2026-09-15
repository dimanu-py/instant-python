{% if general.python_version in ["3.13", "3.12", "3.11"] %}
from typing import TypeVar
{% else %}
from typing import TypeVar, Generic
{% endif %}

from {{ general.source_name }}{{ "shared.domain.value_object.uuid" | resolve_import_path(template.name) }} import Uuid
from {{ general.source_name }}{{ "shared.infra.persistence.sqlalchemy.base" | resolve_import_path(template.name) }} import Base
from {{ general.source_name }}{{ "shared.infra.persistence.sqlalchemy.session_maker" | resolve_import_path(template.name) }} import (
	SessionMaker,
)

Entity = TypeVar("Entity")
{% if general.python_version in ["3.13", "3.12", "3.11"] %}
class SqlAlchemyRepository[Model: Base]:	
{% else %}
Model = TypeVar("Model", bound=Base)
class SqlAlchemyRepository(Generic[Model]):
{% endif %}
	_model_class: type[Model]
	_session_maker: SessionMaker

	def __init__(self, session_maker: SessionMaker, model_class: Type[Model]) -> None:
		self._session_maker = session_maker
		self._model_class = model_class

	def persist(self, entity: Entity) -> None:
		with self._session_maker.get_session() as session:
			entity_model = self._model_class(**entity.to_dict())
			session.add(entity_model)
			session.commit()

	def search_by_id(self, entity_id: Uuid) -> Entity | None:
		with self._session_maker.get_session() as session:
			entity_model = (
				session.query(self._model_class)
				.filter(self._model_class.id == entity_id.value)
				.first()
			)
			return entity_model.to_aggregate() if entity_model else None
