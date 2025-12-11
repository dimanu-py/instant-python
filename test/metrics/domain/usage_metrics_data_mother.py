from instant_python.metrics.domain.usage_metrics_data import UsageMetricsEvent


class UsageMetricsDataMother:
    @staticmethod
    def any() -> UsageMetricsEvent:
        return UsageMetricsEvent(
            ipy_version="1.2.3",
            operating_system="linux",
            python_version="3.12",
            command="init",
            template="clean_architecture",
            built_in_features=["makefile"],
        )
