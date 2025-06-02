from instant_python.configuration.git.git_configuration import GitConfiguration
from test.random_generator import RandomGenerator


class GitConfigurationMother:
    @staticmethod
    def initialize() -> GitConfiguration:
        return GitConfiguration(
            initialize=True,
            username=RandomGenerator.name(),
            email=RandomGenerator.email(),
        )

    @staticmethod
    def not_initialize() -> GitConfiguration:
        return GitConfiguration(initialize=False)

    @classmethod
    def with_parameters(cls, **custom_options) -> GitConfiguration:
        defaults = cls.initialize().to_primitives()
        defaults.update(custom_options)
        return GitConfiguration(**defaults)
