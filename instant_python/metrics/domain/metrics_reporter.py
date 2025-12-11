from abc import ABC, abstractmethod

from instant_python.metrics.domain.usage_metrics_data import UsageMetricsEvent


class MetricsReporter(ABC):
    @abstractmethod
    def send(self, metrics: UsageMetricsEvent) -> None:
        raise NotImplementedError
