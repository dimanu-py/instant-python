from abc import ABC, abstractmethod

from instant_python.metrics.domain.error_metrics_event import ErrorMetricsEvent
from instant_python.metrics.domain.usage_metrics_data import UsageMetricsEvent


class MetricsReporter(ABC):
    @abstractmethod
    def send_success(self, metrics: UsageMetricsEvent) -> None:
        raise NotImplementedError

    @abstractmethod
    def send_error(self, error: Exception, metrics: ErrorMetricsEvent) -> None:
        raise NotImplementedError
