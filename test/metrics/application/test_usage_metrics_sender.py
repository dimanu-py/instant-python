from doublex import Mock, expect_call, ANY_ARG
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.metrics.application.usage_metrics_sender import UsageMetricsSender
from instant_python.metrics.domain.metrics_reporter import MetricsReporter


class TestUsageMetricsSender:
    def test_should_send_usage_metrics_data(self) -> None:
        reporter = Mock(MetricsReporter)
        usage_metrics_sender = UsageMetricsSender(reporter=reporter)

        expect_call(reporter).send(ANY_ARG)

        usage_metrics_sender.execute(command_name="init")

        expect(reporter).to(have_been_satisfied)
