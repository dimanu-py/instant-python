from instant_python.metrics.domain.metrics_reporter import MetricsReporter
from instant_python.shared.domain.config_repository import ConfigRepository


class UsageMetricsSender:
    def __init__(self, repository: ConfigRepository, reporter: MetricsReporter) -> None:
        self._reporter = reporter
        self._repository = repository

    def execute(self, command_name: str) -> None:
        pass
