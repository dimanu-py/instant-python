from abc import ABC, abstractmethod


class ConfigRepository(ABC):
    @abstractmethod
    def read(self, path: str) -> dict:
        raise NotImplementedError
