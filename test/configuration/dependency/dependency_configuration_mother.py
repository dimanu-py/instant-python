from instant_python.configuration.dependency.dependency_configuration import (
    DependencyConfiguration,
)
from test.random_generator import RandomGenerator


class DependencyConfigurationMother:
    @staticmethod
    def any() -> DependencyConfiguration:
        return DependencyConfiguration(
            name=RandomGenerator.word(),
            version=RandomGenerator.version(),
        )

    @classmethod
    def with_parameter(cls, **custom_options) -> DependencyConfiguration:
        defaults = cls.any().to_primitives()
        defaults.update(custom_options)
        return DependencyConfiguration(**defaults)
