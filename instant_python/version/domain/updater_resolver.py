from abc import ABC, abstractmethod

from instant_python.version.domain.installation_method import InstallationMethod
from instant_python.version.domain.updater import Updater


class UpdaterResolver(ABC):
    @abstractmethod
    def resolve(self, installation_method: InstallationMethod) -> Updater:
        raise NotImplementedError
