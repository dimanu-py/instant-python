from abc import ABC, abstractmethod

from instant_python.version.domain.installation_method import InstallationMethod


class InstallationMethodDetector(ABC):
    @abstractmethod
    def detect(self) -> InstallationMethod:
        raise NotImplementedError
