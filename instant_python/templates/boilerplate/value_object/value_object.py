{% if python_version in ["3.13", "3.12", "3.11"] %}
from abc import ABC, abstractmethod
from typing import override

class ValueObject[T](ABC):
	_value: T

	def __init__(self, value: T) -> None:
		self._validate(value)
		self._value = value

	@abstractmethod
	def _validate(self, value: T) -> None: ...

	@property
	def value(self) -> T:
		return self._value

	@override
	def __eq__(self, other: object) -> bool:
		if not isinstance(other, ValueObject):
			return False
		return self.value == other.value
{% else %}
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")

class ValueObject(Generic[T], ABC):
	_value: T

	def __init__(self, value: T) -> None:
		self._validate(value)
		self._value = value
	
	@abstractmethod
	def _validate(self, value: T) -> None: ...
	
	@property
	def value(self) -> T:
		return self._value

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, ValueObject):
			return False
		return self.value == other.value
{% endif %}
