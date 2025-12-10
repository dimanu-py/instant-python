import json
import uuid
from pathlib import Path

from platformdirs import user_config_dir


class UserIdentityManager:
    _CONFIG_FOLDER_NAME = "ipy"
    _METRICS_FILE_NAME = "metrics.json"

    def __init__(self, config_dir: Path | None = None) -> None:
        self._config_dir = Path(
            user_config_dir(
                appname=self._CONFIG_FOLDER_NAME,
            )
        ) if not config_dir else config_dir
        self._metrics_file = self._config_dir / self._METRICS_FILE_NAME

    def get_distinct_id(self) -> str:
        existing_id = self._load_existing_distinct_id()
        return existing_id if existing_id else self._create_and_store_new_distinct_id()

    def _load_existing_distinct_id(self) -> str | None:
        if not self._metrics_file or not self._metrics_file.exists():
            return None

        try:
            content = json.loads(self._metrics_file.read_text())
            distinct_id = content["distinct_id"]
            self._ensure_distinct_id_has_valid_format(distinct_id)
            return distinct_id
        except (json.JSONDecodeError, KeyError, ValueError):
            return None

    @staticmethod
    def _ensure_distinct_id_has_valid_format(distinct_id: str) -> None:
        uuid.UUID(distinct_id)

    def _create_and_store_new_distinct_id(self) -> str:
        new_id = str(uuid.uuid4())
        self._store_distinct_id(new_id)
        return new_id

    def _store_distinct_id(self, distinct_id: str) -> None:
        if not self._metrics_file:
            return

        self._config_dir.mkdir(parents=True, exist_ok=True)
        self._metrics_file.write_text(json.dumps({"distinct_id": distinct_id}))
