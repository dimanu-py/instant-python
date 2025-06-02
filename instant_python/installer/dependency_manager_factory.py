from instant_python.errors.unknown_dependency_manager_error import (
    UnknownDependencyManagerError,
)
from instant_python.installer.dependency_manager import DependencyManager
from instant_python.installer.managers import Managers
from instant_python.installer.pdm_manager import PdmManager
from instant_python.installer.uv_manager import UvManager


class DependencyManagerFactory:
    @staticmethod
    def create(user_manager: str, project_path: str) -> DependencyManager:
        managers = {
            Managers.UV: UvManager,
            Managers.PDM: PdmManager,
        }
        try:
            return managers[Managers(user_manager)](project_path)
        except KeyError:
            raise UnknownDependencyManagerError(user_manager)
