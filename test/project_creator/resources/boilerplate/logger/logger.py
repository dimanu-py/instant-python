from collections.abc import Sequence

import logging
from datetime import date
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path


def create_file_handler(file_name: str, level: int) -> TimedRotatingFileHandler:
	root_project_path = _find_project_root(markers=["pyproject.toml"])
	log_folder = root_project_path / "logs"
	log_folder.mkdir(parents=True, exist_ok=True)

	file_handler = TimedRotatingFileHandler(
		filename=f"{log_folder}/{file_name}_{date.today().isoformat()}.log",
		when="midnight",
		interval=1,
		backupCount=7,
		encoding="utf-8",
	)
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

def _find_project_root(markers: Sequence[str]) -> Path:
	start = Path(__file__).resolve()
	for parent in (start, *start.parents):
		if any((parent / marker).exists() for marker in markers):
			return parent
	raise FileNotFoundError(f"Could not find project root (markers: {markers}).")
