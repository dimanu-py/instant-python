import pytest
{% if dependencies | has_dependency("expects") %}
from expects import expect, equal, raise_error
{% endif %}

from {{ general.source_name }}{{ "shared.domain.errors.incorrect_value_type_error" | resolve_import_path(template.name) }} import (
	IncorrectValueTypeError,
)
from {{ general.source_name }}{{ "shared.domain.errors.invalid_negative_value_error" | resolve_import_path(template.name) }} import (
	InvalidNegativeValueError,
)
from {{ general.source_name }}{{ "shared.domain.errors.required_value_error" | resolve_import_path(template.name) }} import RequiredValueError
from {{ general.source_name }}{{ "shared.domain.value_objects.usables.int_value_object" | resolve_import_path(template.name) }} import (
	IntValueObject,
)
from test{{ "shared.domain.value_objects.int_primitives_mother" | resolve_import_path(template.name) }} import (
	IntPrimitivesMother,
)


@pytest.mark.unit
class TestIntValueObject:
	{% if dependencies | has_dependency("expects") %}
	def test_should_create_int_value_object(self) -> None:
		value = IntPrimitivesMother.any()

		integer = IntValueObject(value)

		expect(integer.value).to(equal(value))

	def test_should_raise_error_when_value_is_none(self) -> None:
		expect(lambda: IntValueObject(None)).to(raise_error(RequiredValueError))

	def test_should_raise_error_when_value_is_not_integer(self) -> None:
		expect(lambda: IntValueObject("123")).to(raise_error(IncorrectValueTypeError))

	def test_should_raise_error_if_int_value_is_negative(self) -> None:
		expect(lambda: IntValueObject(-1)).to(raise_error(InvalidNegativeValueError))

	def test_should_compare_equal_with_same_value(self) -> None:
		common_value = IntPrimitivesMother.any()
		first_integer = IntValueObject(common_value)
		second_integer = IntValueObject(common_value)

		expect(first_integer).to(equal(second_integer))

	def test_should_not_be_equal_with_different_values(self) -> None:
		first_integer = IntValueObject(IntPrimitivesMother.any())
		second_integer = IntValueObject(IntPrimitivesMother.any())

		expect(first_integer).to_not(equal(second_integer))
	{% else %}
	def test_should_create_int_value_object(self) -> None:
		value = IntPrimitivesMother.any()

		integer = IntValueObject(value)

		assert integer.value == value

	def test_should_raise_error_when_value_is_none(self) -> None:
		with pytest.raises(RequiredValueError):
			IntValueObject(None)

	def test_should_raise_error_when_value_is_not_integer(self) -> None:
		with pytest.raises(IncorrectValueTypeError):
			IntValueObject("123")

	def test_should_raise_error_if_int_value_is_negative(self) -> None:
		with pytest.raises(InvalidNegativeValueError):
			IntValueObject(-1)

	def test_should_compare_equal_with_same_value(self) -> None:
		common_value = IntPrimitivesMother.any()
		first_integer = IntValueObject(common_value)
		second_integer = IntValueObject(common_value)

		assert first_integer == second_integer

	def test_should_not_be_equal_with_different_values(self) -> None:
		first_integer = IntValueObject(IntPrimitivesMother.any())
		second_integer = IntValueObject(IntPrimitivesMother.any())

		assert first_integer != second_integer
	{% endif %}
