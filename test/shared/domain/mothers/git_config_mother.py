from instant_python.shared.domain.git_config import GitConfig
from test.random_generator import RandomGenerator


class GitConfigMother:
    @staticmethod
    def initialize() -> GitConfig:
        return GitConfig(
            initialize=True,
            username=RandomGenerator.name(),
            email=RandomGenerator.email(),
        )

    @staticmethod
    def not_initialize() -> GitConfig:
        return GitConfig(initialize=False)

    @classmethod
    def with_parameters(cls, **custom_options) -> GitConfig:
        defaults = cls.initialize().to_primitives()
        defaults.update(custom_options)
        return GitConfig(**defaults)
