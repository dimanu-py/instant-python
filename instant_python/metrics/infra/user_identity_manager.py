import json
import uuid
from pathlib import Path


class UserIdentityManager:
    def __init__(self, config_dir: Path | None = None) -> None:
        self._config_dir = config_dir
        self._metrics_file = self._config_dir / "metrics.json" if config_dir else None

    def get_distinct_id(self) -> str:
        if self._metrics_file and self._metrics_file.exists():
            try:
                content = json.loads(self._metrics_file.read_text())
                return content["distinct_id"]
            except (json.JSONDecodeError, KeyError):
                pass

        distinct_id = str(uuid.uuid4())

        if self._metrics_file:
            self._config_dir.mkdir(parents=True, exist_ok=True)
            self._metrics_file.write_text(json.dumps({"distinct_id": distinct_id}))

        return distinct_id
