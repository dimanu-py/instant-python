import json
import logging


class JSONFormatter(logging.Formatter):
	def format(self, record: logging.LogRecord) -> str:
		log_record = {
			"time": self.formatTime(record, self.datefmt),
			"level": record.levelname,
			"name": record.name,
			"message": record.getMessage(),
		}
		if hasattr(record, "extra"):
			log_record["extra"] = record.extra

		return json.dumps(log_record)