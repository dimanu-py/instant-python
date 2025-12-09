from pathlib import Path
import json

import vcr
from vcr.request import Request

from instant_python.metrics.infra.post_hog_config import PostHogConfig
from instant_python.metrics.infra.post_hog_metric_reporter import PostHogMetricReporter
from test.metrics.domain.usage_metrics_data_mother import UsageMetricsDataMother


def filter_api_key(request) -> Request:
    """Filter api_key from request body before recording"""
    if request.body:
        body = json.loads(request.body.decode('utf-8'))
        body['api_key'] = '****'
        request.body = json.dumps(body).encode('utf-8')
    return request


posthog_vcr = vcr.VCR(
    cassette_library_dir=str(Path(__file__).parent / "cassettes"),
    record_mode="once",
    filter_headers=["Authorization"],
    before_record_request=filter_api_key,
)


class TestPostHogMetricReporter:
    @posthog_vcr.use_cassette("success_posthog_reporter.yml")
    def test_should_send_metrics_to_posthog(self) -> None:
        config = PostHogConfig()
        reporter = PostHogMetricReporter(config=config)
        metrics = UsageMetricsDataMother.any()

        reporter.send(metrics)
