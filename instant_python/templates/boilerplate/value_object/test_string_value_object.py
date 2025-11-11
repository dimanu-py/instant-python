import pytest
{% if dependencies | has_dependency("expects") %}
from expects import expect, equal, raise_error
{% endif %}

from {{ general.source_name }}{{ "shared.domain.errors.incorrect_value_type_error" | resolve_import_path(template.name) }} import (
	IncorrectValueTypeError,
)
from {{ general.source_name }}{{ "shared.domain.errors.required_value_error" | resolve_import_path(template.name) }} import RequiredValueError
from {{ general.source_name }}{{ "shared.domain.value_objects.usables.string_value_object" | resolve_import_path(template.name) }} import (
	StringValueObject,
)
from test{{ "shared.domain.value_objects.string_primitives_mother" | resolve_import_path(template.name) }} import (
	StringPrimitivesMother,
)


@pytest.mark.unit
class TestStringValueObject:
	{% if dependencies | has_dependency("expects") %}
	def test_should_create_string_value_object(self) -> None:
		value = StringPrimitivesMother.any()

		string = StringValueObject(value)

		expect(string.value).to(equal(value))

	def test_should_raise_error_when_value_is_none(self) -> None:
		expect(lambda: StringValueObject(None)).to(raise_error(RequiredValueError))

	def test_should_raise_error_when_value_is_not_string(self) -> None:
		expect(lambda: StringValueObject(123)).to(raise_error(IncorrectValueTypeError))

	def test_should_compare_equal_with_same_value(self) -> None:
		common_value = StringPrimitivesMother.any()
		first_string = StringValueObject(common_value)
		second_string = StringValueObject(common_value)

		expect(first_string).to(equal(second_string))

	def test_should_not_be_equal_with_different_values(self) -> None:
		first_string = StringValueObject(StringPrimitivesMother.any())
		second_string = StringValueObject(StringPrimitivesMother.any())

		expect(first_string).to_not(equal(second_string))
	{% else %}
	def test_should_create_string_value_object(self) -> None:
		value = StringPrimitivesMother.any()

		string = StringValueObject(value)

		assert string.value == value

	def test_should_raise_error_when_value_is_none(self) -> None:
		with pytest.raises(RequiredValueError):
			StringValueObject(None)

	def test_should_raise_error_when_value_is_not_string(self) -> None:
		with pytest.raises(IncorrectValueTypeError):
			StringValueObject(123)

	def test_should_compare_equal_with_same_value(self) -> None:
		common_value = StringPrimitivesMother.any()
		first_string = StringValueObject(common_value)
		second_string = StringValueObject(common_value)

		assert first_string == second_string

	def test_should_not_be_equal_with_different_values(self) -> None:
		first_string = StringValueObject(StringPrimitivesMother.any())
		second_string = StringValueObject(StringPrimitivesMother.any())

		assert first_string != second_string
	{% endif %}