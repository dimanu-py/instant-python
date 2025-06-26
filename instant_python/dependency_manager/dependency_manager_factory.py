from instant_python.dependency_manager.dependency_manager import DependencyManager
from instant_python.dependency_manager.pdm_dependency_manager import PdmDependencyManager
from instant_python.dependency_manager.uv_dependency_manager import UvDependencyManager
from instant_python.errors.unknown_dependency_manager_error import UnknownDependencyManagerError
from instant_python.shared.managers import Managers


class DependencyManagerFactory:
    @staticmethod
    def create(dependency_manager: str, project_directory: str) -> DependencyManager:
        managers = {
            Managers.UV: UvDependencyManager,
            Managers.PDM: PdmDependencyManager,
        }
        try:
            return managers[Managers(dependency_manager)](project_directory)
        except KeyError:
            raise UnknownDependencyManagerError(dependency_manager)
