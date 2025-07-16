{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
import logging

from {{ general.source_name }}.{{ template_infra_import }}.logger.file_rotating_handler import TimeRotatingFileHandler


class FileLogger:
	def __init__(self, name: str, handlers: list[logging.Handler]) -> None:
		self._logger = logging.getLogger(name)
		self._logger.setLevel(logging.DEBUG)

		if not self._logger.hasHandlers():
			self._logger.handlers.extend(handlers)

	def debug(self, message: str, details: dict) -> None:
		self._logger.debug(
			msg=message,
			extra={"details": details},
		)

	def info(self, message: str, details: dict) -> None:
		self._logger.info(
			msg=message,
			extra={"details": details},
		)

	def warning(self, message: str, details: dict) -> None:
		raise NotImplementedError

	def error(self, message: str, details: dict) -> None:
		self._logger.error(
			msg=message,
			extra={"details": details},
		)

	def critical(self, message: str, details: dict) -> None:
		self._logger.critical(
			msg=message,
			extra={"details": details},
		)


def create_file_logger(name: str) -> FileLogger:
	return FileLogger(
		name=name,
		handlers=[
			TimeRotatingFileHandler.create(
				file_name="production",
				level_to_record=logging.ERROR,
			),
			TimeRotatingFileHandler.create(
				file_name="dev",
				level_to_record=logging.DEBUG,
			),
		],
	)
