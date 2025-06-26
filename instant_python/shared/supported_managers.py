from enum import Enum


class SupportedManagers(str, Enum):
    UV = "uv"
    PDM = "pdm"
