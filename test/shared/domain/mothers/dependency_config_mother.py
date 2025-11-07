from instant_python.shared.domain.dependency_config import (
    DependencyConfig,
)
from test.random_generator import RandomGenerator


class DependencyConfigMother:
    @staticmethod
    def any() -> DependencyConfig:
        return DependencyConfig(
            name=RandomGenerator.word(),
            version=RandomGenerator.version(),
        )

    @classmethod
    def with_parameter(cls, **custom_options) -> DependencyConfig:
        defaults = cls.any().to_primitives()
        defaults.update(custom_options)
        return DependencyConfig(**defaults)
