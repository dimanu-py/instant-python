from instant_python.metrics.domain.error_metrics_event import ErrorMetricsEvent


class ErrorMetricsEventMother:
    @staticmethod
    def any() -> ErrorMetricsEvent:
        return ErrorMetricsEvent(
            ipy_version="1.2.3",
            operating_system="linux",
            command="init",
            error_type="ValueError",
            error_message="An error occurred",
        )
