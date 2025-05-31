from dataclasses import dataclass, asdict

from instant_python.configuration.constants import SUPPORTED_DEPENDENCY_MANAGERS, SUPPORTED_PYTHON_VERSIONS, SUPPORTED_LICENSES
from instant_python.configuration.invalid_dependency_manager_value import (
    InvalidDependencyManagerValue,
)
from instant_python.configuration.invalid_license_value import InvalidLicenseValue
from instant_python.configuration.invalid_version_value import InvalidPythonVersionValue


@dataclass
class GeneralConfiguration:
    slug: str
    source_name: str
    description: str
    version: str
    author: str
    license: str
    python_version: str
    dependency_manager: str

    def __post_init__(self) -> None:
        self._ensure_license_is_supported()
        self._ensure_python_version_is_supported()
        self._ensure_dependency_manager_is_supported()

    def _ensure_license_is_supported(self) -> None:
        if self.license not in SUPPORTED_LICENSES:
            raise InvalidLicenseValue(self.license)

    def _ensure_python_version_is_supported(self) -> None:
        if self.python_version not in SUPPORTED_PYTHON_VERSIONS:
            raise InvalidPythonVersionValue(self.python_version)

    def _ensure_dependency_manager_is_supported(self) -> None:
        if self.dependency_manager not in SUPPORTED_DEPENDENCY_MANAGERS:
            raise InvalidDependencyManagerValue(self.dependency_manager)

    def to_primitives(self) -> dict[str, str]:
        return asdict(self)
