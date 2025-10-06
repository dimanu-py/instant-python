from instant_python.config.domain.configuration_schema import ConfigurationSchema
from test.config.domain.mothers.dependency_configuration_mother import DependencyConfigurationMother
from test.config.domain.mothers.general_configuration_mother import GeneralConfigurationMother
from test.config.domain.mothers.git_configuration_mother import GitConfigurationMother
from test.config.domain.mothers.template_configuration_mother import TemplateConfigurationMother


class ConfigurationSchemaMother:
    @staticmethod
    def any() -> ConfigurationSchema:
        return ConfigurationSchema(
            general=GeneralConfigurationMother.any(),
            dependencies=[DependencyConfigurationMother.any() for _ in range(3)],
            template=TemplateConfigurationMother.any(),
            git=GitConfigurationMother.initialize(),
        )
