from abc import ABC, abstractmethod


class ConfigurationRepository(ABC):
    @abstractmethod
    def read(self, path: str) -> dict:
        raise NotImplementedError
