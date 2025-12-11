from pathlib import Path
from typing import Any

from instant_python.metrics.domain.config_snapshot import ConfigSnapshot
from instant_python.shared.domain.config_repository import ConfigRepository
from instant_python.shared.domain.config_schema import ConfigSchema
from instant_python.shared.infra.persistence.yaml_config_repository import ConfigurationFileNotFound


class ConfigSnapshotCreator:
    def __init__(self, repository: ConfigRepository) -> None:
        self._repository = repository

    def execute(self, config_path: Path) -> Any:
        try:
            config = self._read_config_from(config_path)
        except ConfigurationFileNotFound:
            return ConfigSnapshot.unknown()
        return ConfigSnapshot(**config.for_metrics())

    def _read_config_from(self, config_path: Path) -> ConfigSchema:
        return self._repository.read(config_path)
