import platform
from pathlib import Path

from instant_python import __version__
from instant_python.metrics.domain.metrics_reporter import MetricsReporter
from instant_python.metrics.domain.usage_metrics_data import UsageMetricsData
from instant_python.shared.domain.config_repository import ConfigRepository


class UsageMetricsSender:
    def __init__(self, repository: ConfigRepository, reporter: MetricsReporter) -> None:
        self._reporter = reporter
        self._repository = repository

    def execute(self, command_name: str) -> None:
        config = self._extract_config_data_for_metrics()
        metrics_data = UsageMetricsData(
            ipy_version=__version__,
            operating_system=platform.system(),
            python_version=config["python_version"],
            command=command_name,
            template=config["template_type"],
            built_in_features=config["built_in_features"],
        )
        self._send_metrics_report(metrics_data)

    def _send_metrics_report(self, metrics_data: UsageMetricsData) -> None:
        self._reporter.send(metrics_data)

    def _extract_config_data_for_metrics(self) -> dict[str, str | list[str]]:
        config = self._repository.read(Path.cwd() / "ipy.yml")
        return {
            "python_version": config.python_version,
            "template_type": config.template_type,
            "built_in_features": config.template.built_in_features,
        }
