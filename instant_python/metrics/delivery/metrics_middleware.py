import threading
from typing import Any

from click import Context
from typer.core import TyperGroup

from instant_python.metrics.application.config_snapshot_creator import ConfigSnapshotCreator
from instant_python.metrics.application.usage_metrics_sender import UsageMetricsSender
from instant_python.metrics.infra.post_hog_config import PostHogConfig
from instant_python.metrics.infra.post_hog_metrics_reporter import PostHogMetricsReporter
from instant_python.metrics.infra.user_identity_manager import UserIdentityManager
from instant_python.shared.infra.persistence.yaml_config_repository import YamlConfigRepository


class MetricsMiddleware(TyperGroup):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._config_snapshot_creator = ConfigSnapshotCreator(repository=YamlConfigRepository())
        self._metrics_sender = UsageMetricsSender(
            repository=YamlConfigRepository(),
            reporter=PostHogMetricsReporter(
                config=PostHogConfig(),
                user_identity_manager=UserIdentityManager(),
            ),
        )

    def invoke(self, ctx: Context) -> Any:
        try:
            self._execute_command(ctx)
        except Exception as exception:
            raise exception
        finally:
            command = self._extract_executed_command(ctx)
            self._send_metrics_data(command)

    def _execute_command(self, ctx: Context) -> None:
        super().invoke(ctx)

    @staticmethod
    def _extract_executed_command(ctx: Context) -> str:
        return ctx.invoked_subcommand

    def _send_metrics_data(self, command: str) -> None:
        thread = threading.Thread(
            target=self._metrics_sender.execute,
            args=(command,),
            daemon=True,
        )
        thread.start()
        thread.join(timeout=5.0)
