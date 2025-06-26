from enum import Enum


class SupportedLicenses(str, Enum):
    MIT = "MIT"
    APACHE = "Apache"
    GPL = "GPL"

    @classmethod
    def get_supported_licenses(cls) -> list[str]:
        return [license.value for license in cls]
