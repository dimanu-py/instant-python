{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from abc import ABC, abstractmethod
from enum import Enum
{% if general.python_version in ["3.13", "3.12", "3.11"] %}
from typing import override, Self, Any
{% else %}
from typing import Self, Any
from typing_extensions import override
{% endif %}
from inspect import Parameter, _empty, signature

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.value_object import ValueObject
{% else %}
from {{ general.source_name }}.value_objects.value_object import ValueObject
{% endif %}


class Aggregate(ABC):
	@abstractmethod
	def __init__(self) -> None:
		raise NotImplementedError

	@override
	def __repr__(self) -> str:
		attributes = []
		for key, value in sorted(self._to_dict().items()):
			attributes.append(f"{key}={value!r}")

		return f"{self.__class__.__name__}({', '.join(attributes)})"

	@override
	def __eq__(self, other: Self) -> bool:
		if not isinstance(other, self.__class__):
			return NotImplemented

		return self._to_dict() == other._to_dict()

	def _to_dict(self, *, ignore_private: bool = True) -> dict[str, Any]:
		dictionary: dict[str, Any] = {}
		for key, value in self.__dict__.items():
			if ignore_private and key.startswith(f"_{self.__class__.__name__}__"):
				continue  # ignore private attributes

			key = key.replace(f"_{self.__class__.__name__}__", "")

			if key.startswith("_"):
				key = key[1:]

			dictionary[key] = value

		return dictionary

	@classmethod
	def from_primitives(cls, primitives: dict[str, Any]) -> Self:
		if not isinstance(primitives, dict) or not all(
				isinstance(key, str) for key in primitives
		):
			raise TypeError(f'{cls.__name__} primitives <<<{primitives}>>> must be a dictionary of strings. Got <<<{type(primitives).__name__}>>> type.')  # noqa: E501  # fmt: skip

		constructor_signature = signature(obj=cls.__init__)
		parameters: dict[str, Parameter] = {parameter.name: parameter for parameter in constructor_signature.parameters.values() if parameter.name != 'self'}  # noqa: E501  # fmt: skip
		missing = {name for name, parameter in parameters.items() if parameter.default is _empty and name not in primitives}  # noqa: E501  # fmt: skip
		extra = set(primitives) - parameters.keys()

		if missing or extra:
			cls._raise_value_constructor_parameters_mismatch(
				primitives=set(primitives), missing=missing, extra=extra
			)

		return cls(**primitives)

	@classmethod
	def _raise_value_constructor_parameters_mismatch(
			cls,
			primitives: set[str],
			missing: set[str],
			extra: set[str],
	) -> None:
		primitives_names = ", ".join(sorted(primitives))
		missing_names = ", ".join(sorted(missing))
		extra_names = ", ".join(sorted(extra))

		raise ValueError(f'{cls.__name__} primitives <<<{primitives_names}>>> must contain all constructor parameters. Missing parameters: <<<{missing_names}>> and extra parameters: <<<{extra_names}>>>.')  # noqa: E501  # fmt: skip

	def to_primitives(self) -> dict[str, Any]:
		primitives = self._to_dict()
		for key, value in primitives.items():
			if isinstance(value, Aggregate) or hasattr(value, "to_primitives"):
				value = value.to_primitives()

			elif isinstance(value, Enum):
				value = value.value

			elif isinstance(value, ValueObject) or hasattr(value, "value"):
				value = value.value

				if isinstance(value, Enum):
					value = value.value

			primitives[key] = value

		return primitives