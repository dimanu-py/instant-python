from {{ general.source_name }}{{ "shared.domain.errors.incorrect_value_type_error" | resolve_import_path(template.name) }} import IncorrectValueTypeError
from {{ general.source_name }}{{ "shared.domain.errors.required_value_error" | resolve_import_path(template.name) }} import RequiredValueError
from {{ general.source_name }}{{ "shared.domain.value_objects.decorators.validation" | resolve_import_path(template.name) }} import validate
from {{ general.source_name }}{{ "shared.domain.value_objects.value_object" | resolve_import_path(template.name) }} import ValueObject


class StringValueObject(ValueObject[str]):
    @validate
    def _ensure_has_value(self, value: str) -> None:
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_is_string(self, value: str) -> None:
        if not isinstance(value, str):
            raise IncorrectValueTypeError(value)
