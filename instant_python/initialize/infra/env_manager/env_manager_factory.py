from instant_python.initialize.domain.env_manager import EnvManager
from instant_python.initialize.infra.env_manager.pdm_env_manager import PdmEnvManager
from instant_python.initialize.infra.env_manager.uv_env_manager import UvEnvManager
from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes
from instant_python.shared.supported_managers import SupportedManagers


class EnvManagerFactory:
    @staticmethod
    def create(dependency_manager: str, project_directory: str) -> EnvManager:
        managers = {
            SupportedManagers.UV: UvEnvManager,
            SupportedManagers.PDM: PdmEnvManager,
        }
        try:
            return managers[SupportedManagers(dependency_manager)](project_directory)
        except KeyError:
            raise UnknownDependencyManagerError(dependency_manager)


class UnknownDependencyManagerError(ApplicationError):
    def __init__(self, manager: str) -> None:
        message = f"Unknown dependency manager: {manager}. Please use 'pdm' or 'uv'."
        super().__init__(message=message, error_type=ErrorTypes.INSTALLER.value)
