from abc import ABC, abstractmethod

from instant_python.metrics.domain.usage_metrics_data import UsageMetricsData


class MetricReporter(ABC):
    @abstractmethod
    def send(self, metrics: UsageMetricsData) -> None:
        raise NotImplementedError
