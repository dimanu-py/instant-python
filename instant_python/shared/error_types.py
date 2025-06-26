from enum import Enum


class ErrorTypes(str, Enum):
    INSTALLER = "installer_error"
    GENERATOR = "project_generator_error"
    CONFIGURATION = "configuration_error"
