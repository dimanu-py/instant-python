from doublex import Mock, expect_call, ANY_ARG
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.metrics.application.usage_metrics_sender import UsageMetricsSender
from instant_python.metrics.domain.metric_reporter import MetricReporter
from instant_python.shared.domain.config_repository import ConfigRepository
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother


class TestUsageMetricsSender:
    def test_should_send_usage_metrics_data(self) -> None:
        config = ConfigSchemaMother.any()
        usage_metrics = {
            "ipy_version": "1.2.3",
            "operating_system": "linux",
            "python_version": config.python_version,
            "command": "init",
            "template": "clean_architecture",
            "built_in_features": ["makefile"],
            "success": True,
            "error_message": None,
        }
        repository = Mock(ConfigRepository)
        reporter = Mock(MetricReporter)
        usage_metrics_sender = UsageMetricsSender(
            repository=repository,
            reporter=reporter,
        )

        expect_call(repository).read(ANY_ARG).returns(config)
        expect_call(reporter).send(usage_metrics)

        usage_metrics_sender.execute(command_name="init", success=True, error_message=None)

        expect(repository).to(have_been_satisfied)
        expect(reporter).to(have_been_satisfied)
