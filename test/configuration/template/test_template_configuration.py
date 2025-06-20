from expects import expect, raise_error

from instant_python.configuration.template.bounded_context_not_applicable import (
    BoundedContextNotApplicable,
)
from instant_python.configuration.template.bounded_context_not_especified import (
    BoundedContextNotSpecified,
)
from instant_python.configuration.template.invalid_built_in_features_values import (
    InvalidBuiltInFeaturesValues,
)
from instant_python.configuration.template.invalid_template_value import (
    InvalidTemplateValue,
)
from test.configuration.template.template_configuration_mother import (
    TemplateConfigurationMother,
)


class TestTemplateConfiguration:
    def test_should_not_allow_to_create_template_configuration_with_unsupported_template(
        self,
    ) -> None:
        expect(lambda: TemplateConfigurationMother.with_parameters(name="hexagonal_architecture")).to(
            raise_error(InvalidTemplateValue)
        )

    def test_should_not_allow_to_create_template_configuration_with_unsupported_built_in_feature(
        self,
    ) -> None:
        expect(lambda: TemplateConfigurationMother.with_parameters(built_in_features=["javascript"])).to(
            raise_error(InvalidBuiltInFeaturesValues)
        )

    def test_should_not_allow_to_specify_bounded_context_if_template_is_not_ddd(
        self,
    ) -> None:
        expect(
            lambda: TemplateConfigurationMother.with_parameters(
                name="standard_project",
                specify_bounded_context=True,
            )
        ).to(raise_error(BoundedContextNotApplicable))

    def test_should_ensure_bounded_context_info_is_passed_if_specified_bounded_context(
        self,
    ) -> None:
        expect(
            lambda: TemplateConfigurationMother.with_parameters(
                name="domain_driven_design",
                specify_bounded_context=True,
                bounded_context=None,
                aggregate_name=None,
            )
        ).to(raise_error(BoundedContextNotSpecified))
