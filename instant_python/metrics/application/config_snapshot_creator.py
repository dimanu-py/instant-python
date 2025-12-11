from pathlib import Path
from typing import Any

from instant_python.shared.domain.config_repository import ConfigRepository


class ConfigSnapshotCreator:
    def __init__(self, repository: ConfigRepository) -> None:
        self._repository = repository

    def execute(self, config_path: Path) -> Any:
        raise NotImplementedError
