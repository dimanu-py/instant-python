{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
import pytest
{% if dependencies | has_dependency("expects") %}
from expects import expect, equal, raise_error
{% endif %}

{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.incorrect_value_type_error import (
	IncorrectValueTypeError,
)
from {{ general.source_name }}.{{ template_domain_import }}.errors.required_value_error import RequiredValueError
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.usables.string_value_object import (
	StringValueObject,
)
from test.{{ template_domain_import }}.value_objects.string_primitives_mother import (
	StringPrimitivesMother,
)
{% else %}
from {{ general.source_name }}.errors.incorrect_value_type_error import (
	IncorrectValueTypeError,
)
from {{ general.source_name }}.errors.required_value_error import RequiredValueError
from {{ general.source_name }}.value_objects.usables.string_value_object import (
	StringValueObject,
)
from test.value_objects.string_primitives_mother import (
	StringPrimitivesMother,
)
{% endif %}


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