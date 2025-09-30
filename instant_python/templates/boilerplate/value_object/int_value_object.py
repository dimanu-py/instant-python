{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.incorrect_value_type_error import IncorrectValueTypeError
from {{ general.source_name }}.{{ template_domain_import }}.errors.invalid_negative_value_error import InvalidNegativeValueError
from {{ general.source_name }}.{{ template_domain_import }}.errors.required_value_error import RequiredValueError
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.decorators.validation import validate
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.value_object import ValueObject
{% else %}
from {{ general.source_name }}.errors.incorrect_value_type_error import IncorrectValueTypeError
from {{ general.source_name }}.errors.invalid_negative_value_error import InvalidNegativeValueError
from {{ general.source_name }}.errors.required_value_error import RequiredValueError
from {{ general.source_name }}.value_objects.decorators.validation import validate
from {{ general.source_name }}.value_objects.value_object import ValueObject
{% endif %}


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
