{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
import logging
from collections.abc import Sequence
from datetime import date
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Self

{% if template_infra_import %}
from {{ general.source_name }}.{{ template_infra_import }}.logger.json_formatter import JSONFormatter
{% else %}
from {{ general.source_name }}.logger.json_formatter import JSONFormatter
{% endif %}


class TimeRotatingFileHandler(logging.Handler):
	@classmethod
	def create(cls, file_name: str, level_to_record: int) -> Self:
		root_project_path = cls.find_project_root(markers=["pyproject.toml"])
		log_folder = root_project_path / "logs"
		log_folder.mkdir(parents=True, exist_ok=True)

		handler = TimedRotatingFileHandler(
			filename=f"{log_folder}/{file_name}_{date.today().isoformat()}.log",
			when="midnight",
			interval=1,
			backupCount=7,
			encoding="utf-8",
		)
		handler.setFormatter(JSONFormatter())
		handler.setLevel(level_to_record)

		return handler

	@classmethod
	def find_project_root(cls, markers: Sequence[str]) -> Path:
		start = Path(__file__).resolve()
		for parent in (start, *start.parents):
			if any((parent / marker).exists() for marker in markers):
				return parent
		raise FileNotFoundError(f"Could not find project root (markers: {markers}).")
