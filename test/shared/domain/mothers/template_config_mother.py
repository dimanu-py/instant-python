import random

from instant_python.shared.domain.template_config import (
    TemplateConfig,
)


class TemplateConfigMother:
    _SUPPORTED_TEMPLATES = [
        "domain_driven_design",
        "clean_architecture",
        "standard_project",
        "custom",
    ]
    _SUPPORTED_BUILT_IN_FEATURES = [
        "value_objects",
        "github_actions",
        "makefile",
        "logger",
        "event_bus",
        "async_sqlalchemy",
        "async_alembic",
        "fastapi_application",
    ]

    @classmethod
    def any(cls) -> TemplateConfig:
        return TemplateConfig(
            name=random.choice(cls._SUPPORTED_TEMPLATES),
            built_in_features=random.sample(
                cls._SUPPORTED_BUILT_IN_FEATURES,
                k=random.randint(0, len(cls._SUPPORTED_BUILT_IN_FEATURES)),
            ),
        )

    @classmethod
    def with_parameters(cls, **custom_options) -> TemplateConfig:
        defaults = cls.any().to_primitives()
        defaults.update(custom_options)
        return TemplateConfig(**defaults)
