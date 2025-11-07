from abc import ABC, abstractmethod

from instant_python.shared.domain.git_config import GitConfig


class VersionControlConfigurer(ABC):
    @abstractmethod
    def setup(self, config: GitConfig) -> None:
        raise NotImplementedError
