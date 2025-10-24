from abc import ABC, abstractmethod


class ConfigurationRepository(ABC):
    @abstractmethod
    def read_from_file(self, path: str) -> dict:
        raise NotImplementedError
