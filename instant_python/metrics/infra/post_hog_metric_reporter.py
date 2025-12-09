import uuid

from posthog import Posthog

from instant_python.metrics.domain.metric_reporter import MetricReporter
from instant_python.metrics.domain.usage_metrics_data import UsageMetricsData
from instant_python.metrics.infra.post_hog_config import PostHogConfig


class PostHogMetricReporter(MetricReporter):
    def __init__(self, config: PostHogConfig) -> None:
        self._client = Posthog(
            config.api_key,
            host=config.host,
            enable_exception_autocapture=True,
            sync_mode=True,
        )

    def send(self, metrics: UsageMetricsData) -> None:
        self._client.capture(
            distinct_id=uuid.getnode(),
            event="ipy_usage",
            properties=metrics.to_primitives(),
        )
        self._client.flush()
