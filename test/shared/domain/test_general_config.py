import pytest
from expects import expect, raise_error

from instant_python.shared.domain.general_config import (
    InvalidDependencyManagerValue,
    InvalidLicenseValue,
    InvalidPythonVersionValue,
)
from test.shared.domain.mothers.general_config_mother import (
    GeneralConfigMother,
)


class TestGeneralConfig:
    def test_should_allow_to_create_general_config_with_valid_parameters(
        self,
    ) -> None:
        GeneralConfigMother.any()

    @pytest.mark.parametrize(
        "field, value, expected_error",
        [
            pytest.param("license", "BSD", InvalidLicenseValue, id="invalid_license"),
            pytest.param(
                "python_version",
                "3.9",
                InvalidPythonVersionValue,
                id="invalid_python_version",
            ),
            pytest.param(
                "dependency_manager",
                "pip",
                InvalidDependencyManagerValue,
                id="invalid_dependency_manager",
            ),
        ],
    )
    def test_should_raise_error_for_unsupported_config_parameters(self, field, value, expected_error) -> None:
        expect(lambda: GeneralConfigMother.with_parameter(**{field: value})).to(raise_error(expected_error))
