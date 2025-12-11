from posthog import Posthog

from instant_python.metrics.domain.metrics_reporter import MetricsReporter
from instant_python.metrics.domain.usage_metrics_data import UsageMetricsData
from instant_python.metrics.infra.post_hog_config import PostHogConfig
from instant_python.metrics.infra.user_identity_manager import UserIdentityManager


class PostHogMetricsReporter(MetricsReporter):
    def __init__(self, config: PostHogConfig, user_identity_manager: UserIdentityManager) -> None:
        self._client = Posthog(
            config.api_key,
            host=config.host,
            enable_exception_autocapture=True,
            sync_mode=True,
        )
        self._user_identity_manager = user_identity_manager

    def send(self, metrics: UsageMetricsData) -> None:
        try:
            self._client.capture(
                distinct_id=self._user_identity_manager.get_or_create_distinct_id(),
                event="ipy_usage",
                properties=metrics.to_primitives(),
            )
            self._client.flush()
        except Exception:
            pass  # Fire and forget strategy to avoid impacting user experience
