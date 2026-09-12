from enum import Enum


class InstallationMethod(Enum):
    BINARY = "binary"
    PIPX = "pipx"
    UV = "uv"
    PIP = "pip"
