from instant_python.metrics.domain.usage_metrics_data import UsageMetricsData


class UsageMetricsDataMother:
    @staticmethod
    def any() -> UsageMetricsData:
        return UsageMetricsData(
            ipy_version="1.2.3",
            operating_system="linux",
            python_version="3.12",
            command="init",
            success=True,
            template="clean_architecture",
            built_in_features=["makefile"],
            error_message=None,
        )
