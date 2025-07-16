{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.incorrect_value_type_error import IncorrectValueTypeError
from {{ general.source_name }}.{{ template_domain_import }}.errors.required_value_error import RequiredValueError
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.decorators.validation import validate
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.value_object import ValueObject


class StringValueObject(ValueObject[str]):
    @validate
    def _ensure_has_value(self, value: str) -> None:
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_is_string(self, value: str) -> None:
        if not isinstance(value, str):
            raise IncorrectValueTypeError(value)
