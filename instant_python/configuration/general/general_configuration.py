from datetime import datetime
from dataclasses import dataclass, asdict, field
from typing import ClassVar

from instant_python.configuration.general.invalid_dependency_manager_value import (
    InvalidDependencyManagerValue,
)
from instant_python.configuration.general.invalid_license_value import (
    InvalidLicenseValue,
)
from instant_python.configuration.general.invalid_python_version_value import (
    InvalidPythonVersionValue,
)
from instant_python.shared.supported_licenses import SupportedLicenses
from instant_python.shared.supported_managers import SupportedManagers
from instant_python.shared.supported_python_versions import SupportedPythonVersions


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
    year: int = field(default=datetime.now().year)

    _SUPPORTED_DEPENDENCY_MANAGERS: ClassVar[list[str]] = SupportedManagers.get_supported_managers()
    _SUPPORTED_PYTHON_VERSIONS: ClassVar[list[str]] = SupportedPythonVersions.get_supported_versions()
    _SUPPORTED_LICENSES: ClassVar[list[str]] = SupportedLicenses.get_supported_licenses()

    def __post_init__(self) -> None:
        self.version = str(self.version)
        self.python_version = str(self.python_version)
        self._remove_white_spaces_from_slug_if_present()
        self._ensure_license_is_supported()
        self._ensure_python_version_is_supported()
        self._ensure_dependency_manager_is_supported()

    def _remove_white_spaces_from_slug_if_present(self) -> None:
        if " " in self.slug:
            self.slug = self.slug.replace(" ", "")

    def _ensure_license_is_supported(self) -> None:
        if self.license not in self._SUPPORTED_LICENSES:
            raise InvalidLicenseValue(self.license, self._SUPPORTED_LICENSES)

    def _ensure_python_version_is_supported(self) -> None:
        if self.python_version not in self._SUPPORTED_PYTHON_VERSIONS:
            raise InvalidPythonVersionValue(self.python_version, self._SUPPORTED_PYTHON_VERSIONS)

    def _ensure_dependency_manager_is_supported(self) -> None:
        if self.dependency_manager not in self._SUPPORTED_DEPENDENCY_MANAGERS:
            raise InvalidDependencyManagerValue(self.dependency_manager, self._SUPPORTED_DEPENDENCY_MANAGERS)

    def to_primitives(self) -> dict[str, str]:
        return asdict(self)
