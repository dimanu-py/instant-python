from enum import Enum


class SupportedManagers(str, Enum):
    UV = "uv"
    PDM = "pdm"

    @classmethod
    def get_supported_managers(cls) -> list[str]:
        return [manager.value for manager in cls]
