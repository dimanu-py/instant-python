import random

from instant_python.configuration.general.general_configuration import GeneralConfiguration
from test.random_generator import RandomGenerator


SUPPORTED_DEPENDENCY_MANAGERS = ["uv", "pdm"]
SUPPORTED_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13"]
SUPPORTED_LICENSES = ["MIT", "Apache", "GPL"]


class GeneralConfigurationMother:

    @staticmethod
    def any() -> GeneralConfiguration:
        return GeneralConfiguration(
	        slug=RandomGenerator.word(),
	        source_name=RandomGenerator.word(),
	        description=RandomGenerator.description(),
	        version=RandomGenerator.version(),
	        author=RandomGenerator.name(),
	        license=random.choice(SUPPORTED_LICENSES),
	        python_version=random.choice(SUPPORTED_PYTHON_VERSIONS),
	        dependency_manager=random.choice(SUPPORTED_DEPENDENCY_MANAGERS),
        )
    
    @classmethod
    def with_parameter(cls, **custom_options) -> GeneralConfiguration:
        defaults = cls.any().to_primitives()
        defaults.update(custom_options)
        return GeneralConfiguration(**defaults)
