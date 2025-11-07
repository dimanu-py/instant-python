from instant_python.shared.domain.config_schema import ConfigSchema
from test.shared.domain.mothers.dependency_config_mother import DependencyConfigMother
from test.shared.domain.mothers.general_config_mother import GeneralConfigMother
from test.shared.domain.mothers.git_config_mother import GitConfigMother
from test.shared.domain.mothers.template_config_mother import TemplateConfigMother


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

    @staticmethod
    def without_git() -> ConfigSchema:
        return ConfigSchema(
            general=GeneralConfigMother.any(),
            dependencies=[DependencyConfigMother.any() for _ in range(3)],
            template=TemplateConfigMother.any(),
            git=GitConfigMother.not_initialize(),
        )
