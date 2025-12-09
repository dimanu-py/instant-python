from abc import ABC, abstractmethod


class MetricReporter(ABC):
    @abstractmethod
    def send(self, metrics: dict) -> None:
        raise NotImplementedError
