from instant_python.metrics.domain.metric_reporter import MetricReporter
from instant_python.metrics.infra.post_hog_config import PostHogConfig


class PostHogMetricReporter(MetricReporter):
    def __init__(self, config: PostHogConfig) -> None: ...

    def send(self, metrics: dict) -> None:
        raise NotImplementedError
