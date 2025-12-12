import platform

from instant_python import __version__
from instant_python.metrics.domain.config_snapshot import ConfigSnapshot
from instant_python.metrics.domain.error_metrics_event import ErrorMetricsEvent
from instant_python.metrics.domain.metrics_reporter import MetricsReporter
from instant_python.metrics.domain.usage_metrics_data import UsageMetricsEvent


class UsageMetricsSender:
    def __init__(self, reporter: MetricsReporter) -> None:
        self._reporter = reporter

    def execute_on_success(self, command_name: str, config_snapshot: ConfigSnapshot) -> None:
        config = config_snapshot.to_primitives()
        metrics_event = UsageMetricsEvent(
            ipy_version=__version__,
            operating_system=platform.system(),
            command=command_name,
            python_version=config["python_version"],
            dependency_manager=config["dependency_manager"],
            template=config["template_type"],
            built_in_features=config["built_in_features"],
        )
        self._send_metrics_report(metrics_event)

    def execute_on_failure(self, command_name: str, error: Exception) -> None:
        error_event = ErrorMetricsEvent(
            ipy_version=__version__,
            operating_system=platform.system(),
            command=command_name,
            error_type=type(error).__name__,
            error_message=str(error),
        )
        self._send_error_report(error, error_event)

    def _send_metrics_report(self, metrics_data: UsageMetricsEvent) -> None:
        self._reporter.send_success(metrics_data)

    def _send_error_report(self, error: Exception, error_event: ErrorMetricsEvent) -> None:
        self._reporter.send_error(error, error_event)
