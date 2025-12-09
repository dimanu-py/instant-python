import uuid
from pathlib import Path


class UserIdentityManager:
    def __init__(self, config_dir: Path | None = None) -> None:
        self._config_dir = config_dir

    def get_distinct_id(self) -> str:
        return str(uuid.uuid4())
