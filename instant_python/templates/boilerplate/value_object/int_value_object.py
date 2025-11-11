from {{ general.source_name }}{{ "shared.domain.errors.incorrect_value_type_error" | resolve_import_path(template.name) }} import IncorrectValueTypeError
from {{ general.source_name }}{{ "shared.domain.errors.invalid_negative_value_error" | resolve_import_path(template.name) }} import InvalidNegativeValueError
from {{ general.source_name }}{{ "shared.domain.errors.required_value_error" | resolve_import_path(template.name) }} import RequiredValueError
from {{ general.source_name }}{{ "shared.domain.value_objects.decorators.validation" | resolve_import_path(template.name) }} import validate
from {{ general.source_name }}{{ "shared.domain.value_objects.value_object" | resolve_import_path(template.name) }} import ValueObject


class IntValueObject(ValueObject[int]):
    @validate
    def _ensure_has_value(self, value: int) -> None:
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_value_is_integer(self, value: int) -> None:
        if not isinstance(value, int):
            raise IncorrectValueTypeError(value)

    @validate
    def _ensure_value_is_positive(self, value: int) -> None:
        if value < 0:
            raise InvalidNegativeValueError(value)
