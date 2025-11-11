import pytest
{% if dependencies | has_dependency("expects") %}
from expects import expect, equal, raise_error
{% endif %}

from {{ general.source_name }}{{ "shared.domain.errors.incorrect_value_type_error" | resolve_import_path(template.name) }} import (
	IncorrectValueTypeError,
)
from {{ general.source_name }}{{ "shared.domain.errors.invalid_id_format_error" | resolve_import_path(template.name) }} import (
	InvalidIdFormatError,
)
from {{ general.source_name }}{{ "shared.domain.errors.required_value_error" | resolve_import_path(template.name) }} import RequiredValueError
from {{ general.source_name }}{{ "shared.domain.value_objects.usables.uuid" | resolve_import_path(template.name) }} import (
	Uuid,
)
from test{{ "shared.domain.value_objects.uuid_primitives_mother" | resolve_import_path(template.name) }} import (
	UuidPrimitivesMother,
)


@pytest.mark.unit
class TestUuidValueObject:
	{% if dependencies | has_dependency("expects") %}
	def test_should_create_uuid_value_object(self) -> None:
		value = UuidPrimitivesMother.any()

		uuid = Uuid(value)

		expect(uuid.value).to(equal(value))

	def test_should_raise_error_when_value_is_none(self) -> None:
		expect(lambda: Uuid(None)).to(raise_error(RequiredValueError))

	def test_should_raise_error_when_value_is_not_string(self) -> None:
		expect(lambda: Uuid(123)).to(raise_error(IncorrectValueTypeError))

	def test_should_raise_error_when_value_is_not_valid_uuid(self) -> None:
		invalid_uuid = UuidPrimitivesMother.invalid()
		expect(lambda: Uuid(invalid_uuid)).to(raise_error(InvalidIdFormatError))

	def test_should_compare_equal_with_same_value(self) -> None:
		common_value = UuidPrimitivesMother.any()
		first_uuid = Uuid(common_value)
		second_uuid = Uuid(common_value)

		expect(first_uuid).to(equal(second_uuid))

	def test_should_not_be_equal_with_different_values(self) -> None:
		first_uuid = Uuid(UuidPrimitivesMother.any())
		second_uuid = Uuid(UuidPrimitivesMother.any())

		expect(first_uuid).to_not(equal(second_uuid))

	{% else %}
	def test_should_create_uuid_value_object(self) -> None:
		value = UuidPrimitivesMother.any()

		uuid = Uuid(value)

		assert uuid.value == value

	def test_should_raise_error_when_value_is_none(self) -> None:
		with pytest.raises(RequiredValueError):
			Uuid(None)

	def test_should_raise_error_when_value_is_not_string(self) -> None:
		with pytest.raises(IncorrectValueTypeError):
			Uuid(123)

	def test_should_raise_error_when_value_is_not_valid_uuid(self) -> None:
		invalid_uuid = UuidPrimitivesMother.invalid()
		with pytest.raises(InvalidIdFormatError):
			Uuid(invalid_uuid)

	def test_should_compare_equal_with_same_value(self) -> None:
		common_value = UuidPrimitivesMother.any()
		first_uuid = Uuid(common_value)
		second_uuid = Uuid(common_value)

		assert first_uuid == second_uuid

	def test_should_not_be_equal_with_different_values(self) -> None:
		first_uuid = Uuid(UuidPrimitivesMother.any())
		second_uuid = Uuid(UuidPrimitivesMother.any())

		assert first_uuid != second_uuid
	{% endif %}
