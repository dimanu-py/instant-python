from pathlib import Path
from typing import Any

from instant_python.metrics.domain.config_snapshot import ConfigSnapshot
from instant_python.shared.domain.config_repository import ConfigRepository


class ConfigSnapshotCreator:
    def __init__(self, repository: ConfigRepository) -> None:
        self._repository = repository

    def execute(self, config_path: Path) -> Any:
        config = self._read_config_and_filter_metrics_values(config_path)
        return ConfigSnapshot(**config)

    def _read_config_and_filter_metrics_values(self, config_path: Path) -> dict[str, str | list[str]]:
        config = self._repository.read(config_path)
        return config.for_metrics()
