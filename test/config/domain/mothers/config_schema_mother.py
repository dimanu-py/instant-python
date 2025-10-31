from instant_python.config.domain.config_schema import ConfigSchema
from test.config.domain.mothers.dependency_config_mother import DependencyConfigMother
from test.config.domain.mothers.general_config_mother import GeneralConfigMother
from test.config.domain.mothers.git_config_mother import GitConfigMother
from test.config.domain.mothers.template_config_mother import TemplateConfigMother


class ConfigSchemaMother:
    @staticmethod
    def any() -> ConfigSchema:
        return ConfigSchema(
            general=GeneralConfigMother.any(),
            dependencies=[DependencyConfigMother.any() for _ in range(3)],
            template=TemplateConfigMother.any(),
            git=GitConfigMother.initialize(),
        )

    @staticmethod
    def with_template(template: str) -> ConfigSchema:
        return ConfigSchema(
            general=GeneralConfigMother.any(),
            dependencies=[DependencyConfigMother.any() for _ in range(3)],
            template=TemplateConfigMother.with_parameters(name=template),
            git=GitConfigMother.initialize(),
        )
