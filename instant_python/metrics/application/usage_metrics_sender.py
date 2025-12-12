import platform

from instant_python import __version__
from instant_python.metrics.domain.config_snapshot import ConfigSnapshot
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

    def _send_metrics_report(self, metrics_data: UsageMetricsEvent) -> None:
        self._reporter.send(metrics_data)
