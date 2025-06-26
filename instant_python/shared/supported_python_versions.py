from enum import Enum


class SupportedPythonVersions(str, Enum):
    PYTHON_3_10 = "3.10"
    PYTHON_3_11 = "3.11"
    PYTHON_3_12 = "3.12"
    PYTHON_3_13 = "3.13"

    @classmethod
    def get_supported_versions(cls) -> list[str]:
        return [version.value for version in cls]
