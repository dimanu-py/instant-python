import random

from instant_python.config.domain.general_config import (
    GeneralConfig,
)
from test.random_generator import RandomGenerator


class GeneralConfigMother:
    _SUPPORTED_DEPENDENCY_MANAGERS = ["uv", "pdm"]
    _SUPPORTED_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13"]
    _SUPPORTED_LICENSES = ["MIT", "Apache", "GPL"]

    @classmethod
    def any(cls) -> GeneralConfig:
        return GeneralConfig(
            slug=RandomGenerator.word(),
            source_name=RandomGenerator.word(),
            description=RandomGenerator.description(),
            version=RandomGenerator.version(),
            author=RandomGenerator.name(),
            license=random.choice(cls._SUPPORTED_LICENSES),
            python_version=random.choice(cls._SUPPORTED_PYTHON_VERSIONS),
            dependency_manager=random.choice(cls._SUPPORTED_DEPENDENCY_MANAGERS),
        )

    @classmethod
    def with_parameter(cls, **custom_options) -> GeneralConfig:
        defaults = cls.any().to_primitives()
        defaults.update(custom_options)
        return GeneralConfig(**defaults)
