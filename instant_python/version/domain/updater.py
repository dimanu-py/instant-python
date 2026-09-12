from abc import ABC, abstractmethod

LATEST_VERSION = "latest"


class Updater(ABC):
    @abstractmethod
    def update(self, version: str) -> None:
        raise NotImplementedError
