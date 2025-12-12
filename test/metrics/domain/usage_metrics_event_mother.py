from instant_python.metrics.domain.usage_metrics_data import UsageMetricsEvent


class UsageMetricsEventMother:
    @staticmethod
    def any() -> UsageMetricsEvent:
        return UsageMetricsEvent(
            ipy_version="1.2.3",
            operating_system="linux",
            command="init",
            python_version="3.12",
            dependency_manager="uv",
            template="clean_architecture",
            built_in_features=["makefile"],
        )
