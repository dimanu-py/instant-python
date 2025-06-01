import random

from instant_python.configuration.template.template_configuration import (
    TemplateConfiguration,
)


SUPPORTED_TEMPLATES = [
    "domain_driven_design",
    "clean_architecture",
    "standard_project",
    "custom",
]
SUPPORTED_BUILT_IN_FEATURES = [
    "value_objects",
    "github_actions",
    "makefile",
    "logger",
    "event_bus",
    "async_sqlalchemy",
    "async_alembic",
    "fastapi_application",
]


class TemplateConfigurationMother:
    @staticmethod
    def any() -> TemplateConfiguration:
        return TemplateConfiguration(
            name=random.choice(SUPPORTED_TEMPLATES),
            built_in_features=random.sample(
                SUPPORTED_BUILT_IN_FEATURES,
                k=random.randint(0, len(SUPPORTED_BUILT_IN_FEATURES)),
            ),
        )

    @classmethod
    def with_parameters(cls, **custom_options) -> TemplateConfiguration:
        defaults = cls.any().to_primitives()
        defaults.update(custom_options)
        return TemplateConfiguration(**defaults)
