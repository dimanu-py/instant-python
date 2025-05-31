from dataclasses import dataclass

from instant_python.configuration.invalid_license_value import InvalidLicenseValue
from instant_python.configuration.invalid_version_value import InvalidPythonVersionValue

SUPPORTED_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13"]
SUPPORTED_LICENSES = ["MIT", "Apache", "GPL"]


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

    def _ensure_license_is_supported(self) -> None:
        if self.license not in SUPPORTED_LICENSES:
            raise InvalidLicenseValue(self.license)

    def _ensure_python_version_is_supported(self) -> None:
        if self.python_version not in SUPPORTED_PYTHON_VERSIONS:
            raise InvalidPythonVersionValue(self.python_version)
