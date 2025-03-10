from src.installer.dependency_manager import DependencyManager
from src.installer.managers import Managers
from src.installer.pdm_manager import PdmManager
from src.installer.uv_manager import UvManager


class DependencyManagerFactory:
    @staticmethod
    def create(user_manager: str, project_path: str) -> DependencyManager:
        managers = {
            Managers.UV: UvManager,
            Managers.PDM: PdmManager,
        }
        return managers[Managers(user_manager)](project_path)
