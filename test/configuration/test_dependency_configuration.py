from expects import expect, be_true, be_false, be_none, be

from test.configuration.dependency_configuration_mother import (
    DependencyConfigurationMother,
)


class TestDependencyConfiguration:
    def test_should_allow_to_create_dev_dependency_configuration(self) -> None:
        dependency_configuration = DependencyConfigurationMother.with_parameter(
            is_dev=True
        )

        expect(dependency_configuration.is_dev).to(be_true)

    def test_should_allow_to_create_non_dev_dependency_configuration(self) -> None:
        dependency_configuration = DependencyConfigurationMother.any()

        expect(dependency_configuration.is_dev).to(be_false)

    def test_should_allow_to_create_dependency_configuration_with_group(self) -> None:
        dependency_configuration = DependencyConfigurationMother.with_parameter(
            group="test"
        )

        expect(dependency_configuration.group).to_not(be_none)
        
    def test_should_allow_to_create_dependency_configuration_without_group(self) -> None:
        dependency_configuration = DependencyConfigurationMother.any()

        expect(dependency_configuration.group).to(be(""))
