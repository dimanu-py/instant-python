from instant_python.metrics.domain.metric_reporter import MetricReporter
from instant_python.shared.domain.config_repository import ConfigRepository


class UsageMetricsSender:
    def __init__(self, repository: ConfigRepository, reporter: MetricReporter) -> None:
        self._reporter = reporter
        self._repository = repository

    def execute(self, command_name: str, success: bool, error_message: str | None) -> None:
        pass
