from dataclasses import dataclass, asdict
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

    _SUPPORTED_DEPENDENCY_MANAGERS: ClassVar[list[str]] = ["uv", "pdm"]
    _SUPPORTED_PYTHON_VERSIONS: ClassVar[list[str]] = ["3.10", "3.11", "3.12", "3.13"]
    _SUPPORTED_LICENSES: ClassVar[list[str]] = ["MIT", "Apache", "GPL"]

    def __post_init__(self) -> None:
        self.version = str(self.version)
        self.python_version = str(self.python_version)
        self._ensure_license_is_supported()
        self._ensure_python_version_is_supported()
        self._ensure_dependency_manager_is_supported()

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
