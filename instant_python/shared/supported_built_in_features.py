from enum import Enum


class SupportedBuiltInFeatures(str, Enum):
    VALUE_OBJECTS = "value_objects"
    GITHUB_ACTIONS = "github_actions"
    GITHUB_ISSUES_TEMPLATE = "github_issues_template"
    MAKEFILE = "makefile"
    LOGGER = "logger"
    EVENT_BUS = "event_bus"
    ASYNC_SQLALCHEMY = "async_sqlalchemy"
    ASYNC_ALEMBIC = "async_alembic"
    FASTAPI = "fastapi_application"
    PRECOMMIT = "precommit_hook"
    CITATION = "citation_file"
    SECURITY = "security_file"

    @classmethod
    def get_supported_built_in_features(cls) -> list[str]:
        return [feature.value for feature in cls]
