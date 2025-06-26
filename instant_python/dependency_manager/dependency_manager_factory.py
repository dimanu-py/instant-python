from instant_python.dependency_manager.dependency_manager import DependencyManager
from instant_python.dependency_manager.pdm_dependency_manager import PdmDependencyManager
from instant_python.dependency_manager.uv_dependency_manager import UvDependencyManager
from instant_python.dependency_manager.unknown_dependency_manager_error import UnknownDependencyManagerError
from instant_python.shared.supported_managers import SupportedManagers


class DependencyManagerFactory:
    @staticmethod
    def create(dependency_manager: str, project_directory: str) -> DependencyManager:
        managers = {
            SupportedManagers.UV: UvDependencyManager,
            SupportedManagers.PDM: PdmDependencyManager,
        }
        try:
            return managers[SupportedManagers(dependency_manager)](project_directory)
        except KeyError:
            raise UnknownDependencyManagerError(dependency_manager)
