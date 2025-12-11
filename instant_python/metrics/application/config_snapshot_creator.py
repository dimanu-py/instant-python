from pathlib import Path
from typing import Any


class ConfigSnapshotCreator:
    def execute(self, config_path: Path) -> Any:
        raise NotImplementedError
