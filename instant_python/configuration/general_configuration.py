from dataclasses import dataclass

from instant_python.configuration.invalid_license_value import InvalidLicenseValue

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

    def _ensure_license_is_supported(self) -> None:
        if self.license not in SUPPORTED_LICENSES:
            raise InvalidLicenseValue(self.license)
