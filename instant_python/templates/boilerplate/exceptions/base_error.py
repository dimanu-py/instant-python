from abc import ABC


class BaseError(Exception, ABC):
	"""Base class for all controlled errors in the application."""

	def __init__(self, message: str) -> None:
		self._message = message
		super().__init__(self._message)

	@property
	def message(self) -> str:
		return self._message
