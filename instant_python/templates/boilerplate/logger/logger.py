{% set template_infra_import = "shared.infra"|compute_base_path(template) %}
import logging
from datetime import date
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from {{ source_name }}.{{ template_infra_import }}.log.json_formatter import JSONFormatter


def create_file_handler(file_name: str, level: int) -> TimedRotatingFileHandler:
	root_project_path = Path(__file__).parents[4]
	log_folder = root_project_path / "logs"
	log_folder.mkdir(parents=True, exist_ok=True)

	file_handler = TimedRotatingFileHandler(
		filename=f"{log_folder}/{file_name}_{date.today().isoformat()}.log",
		when="midnight",
		interval=1,
		backupCount=7,
		encoding="utf-8",
	)
	file_handler.setFormatter(JSONFormatter())
	file_handler.setLevel(level)

	return file_handler


def create_logger(logger_name: str) -> logging.Logger:
	logger = logging.getLogger(logger_name)
	logger.setLevel(logging.DEBUG)

	production_handler = create_file_handler(file_name="prod", level=logging.ERROR)
	develop_handler = create_file_handler(file_name="dev", level=logging.DEBUG)

	if not logger.handlers:
		logger.addHandler(production_handler)
		logger.addHandler(develop_handler)

	return logger