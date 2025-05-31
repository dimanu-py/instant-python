from expects import expect, raise_error

from instant_python.configuration.invalid_dependency_manager_value import InvalidDependencyManagerValue
from instant_python.configuration.invalid_license_value import InvalidLicenseValue
from instant_python.configuration.invalid_version_value import InvalidPythonVersionValue
from test.configuration.general_configuration_mother import GeneralConfigurationMother


class TestGeneralConfiguration:
    def test_should_not_allow_to_create_general_configuration_with_invalid_license(
        self,
    ) -> None:
        expect(lambda: GeneralConfigurationMother.with_parameter(license="BSD")).to(
            raise_error(InvalidLicenseValue)
        )

    def test_should_not_allow_to_create_general_configuration_with_invalid_python_version(
        self,
    ) -> None:
        expect(
            lambda: GeneralConfigurationMother.with_parameter(python_version="3.9")
        ).to(raise_error(InvalidPythonVersionValue))
        
    def test_should_not_allow_to_create_general_configuration_with_invalid_dependency_manager(
        self,
    ) -> None:
        expect(
            lambda: GeneralConfigurationMother.with_parameter(dependency_manager="pip")
        ).to(raise_error(InvalidDependencyManagerValue))
