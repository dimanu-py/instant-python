from enum import Enum


class Managers(str, Enum):
    PYENV = "pyenv"
    UV = "uv"
    PDM = "pdm"
