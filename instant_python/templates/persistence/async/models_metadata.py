"""
This  module is needed for alembic to detect correctly all models of the project.

When we import Base.metadata in the env.py file it will include all the models that inherit from it only if these models
have already been imported. To keep the env.py file clean, we import the Base.metadata in this file and then import all the
needed models.
"""
from {{ general.source_name }}{{ "shared.infra.persistence.sqlalchemy.base" | resolve_import_path(template.name) }} import Base

base = Base