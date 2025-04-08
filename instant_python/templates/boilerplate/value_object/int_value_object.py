{% set template_domain_import = "shared.domain"|compute_base_path(template) %}
from {{ source_name }}.{{ template_domain_import }}.exceptions.invalid_negative_value_error import (
	InvalidNegativeValueError,
)
from {{ source_name }}.{{ template_domain_import }}.value_object.value_object import ValueObject


class IntValueObject(ValueObject[int]):
	def _validate(self, value: int) -> None:
		if value < 0:
			raise InvalidNegativeValueError(value)
