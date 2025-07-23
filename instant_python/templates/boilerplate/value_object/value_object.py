{% if general.python_version in ["3.13", "3.12", "3.11"] %}
from abc import ABC
from collections.abc import Callable
from typing import override, Self

class ValueObject[T](ABC):
	__slots__ = ("_value",)
	__match_args__ = ("_value",)

	_value: T

	def __init__(self, value: T) -> None:
		self._validate(value)
		object.__setattr__(self, "_value", value)

	def _validate(self, value: T) -> None:
		"""Gets all methods decorated with @validate and calls them to validate all domain conditions."""
		validators: list[Callable[[T], None]] = []
		for cls in reversed(self.__class__.__mro__):
			if cls is object:
				continue
			for name, member in cls.__dict__.items():
				if getattr(member, "_is_validator", False):
					validators.append(getattr(self, name))

		for validator in validators:
			validator(value)

	@property
	def value(self) -> T:
		return self._value

	@override
	def __eq__(self, other: Self) -> bool:
		return self.value == other.value

	@override
	def __repr__(self) -> str:
		return f"{self.__class__.__name__}({self._value!r})"

	@override
	def __str__(self) -> str:
		return str(self._value)

	@override
	def __hash__(self) -> int:
		return hash(self._value)

	@override
	def __setattr__(self, name: str, value: T) -> None:
		"""Prevents modification of the value after initialization."""
		if name in self.__slots__:
			raise AttributeError("Cannot modify the value of a ValueObject")

		public_name = name.replace("_", "")
		public_slots = [slot.replace("_", "") for slot in self.__slots__]
		if public_name in public_slots:
			raise AttributeError("Cannot modify the value of a ValueObject")

		raise AttributeError(
			f"Class {self.__class__.__name__} object has no attribute '{name}'"
		)
{% else %}
from abc import ABC
from typing import TypeVar, Generic
from typing_extensions import override

T = TypeVar("T")

class ValueObject(Generic[T], ABC):
	__slots__ = ("_value",)
	__match_args__ = ("_value",)

	_value: T
	
	def __init__(self, value: T) -> None:
		self._validate(value)
		object.__setattr__(self, "_value", value)
	
	def _validate(self, value: T) -> None:
		"""Gets all methods decorated with @validate and calls them to validate all domain conditions."""
		validators: list[Callable[[T], None]] = []
		for cls in reversed(self.__class__.__mro__):
			if cls is object:
				continue
			for name, member in cls.__dict__.items():
				if getattr(member, "_is_validator", False):
					validators.append(getattr(self, name))
	
		for validator in validators:
			validator(value)
	
	@property
	def value(self) -> T:
		return self._value
	
	@override
	def __eq__(self, other: Self) -> bool:
		return self.value == other.value
	
	@override
	def __repr__(self) -> str:
		return f"{self.__class__.__name__}({self._value!r})"
	
	@override
	def __str__(self) -> str:
		return str(self._value)

	@override
	def __hash__(self) -> int:
		return hash(self._value)
	
	@override
	def __setattr__(self, name: str, value: T) -> None:
		"""Prevents modification of the value after initialization."""
		if name in self.__slots__:
			raise AttributeError("Cannot modify the value of a ValueObject")
	
		public_name = name.replace("_", "")
		public_slots = [slot.replace("_", "") for slot in self.__slots__]
		if public_name in public_slots:
			raise AttributeError("Cannot modify the value of a ValueObject")
	
		raise AttributeError(
			f"Class {self.__class__.__name__} object has no attribute '{name}'"
		)
{% endif %}
