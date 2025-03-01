from {{ source_name }}.shared.domain.exceptions.invalid_negative_value_error import (
	InvalidNegativeValueError,
)
from {{ source_name }}.shared.domain.value_objects.value_object import ValueObject


class IntValueObject(ValueObject[int]):
	def _validate(self, value: int) -> None:
		if value < 0:
			raise InvalidNegativeValueError(value)
