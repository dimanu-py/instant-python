{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.incorrect_value_type_error import IncorrectValueTypeError
from {{ general.source_name }}.{{ template_domain_import }}.errors.invalid_id_format_error import InvalidIdFormatError
from {{ general.source_name }}.{{ template_domain_import }}.errors.required_value_error import RequiredValueError
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.decorators.validation import validate
from {{ general.source_name }}.{{ template_domain_import }}.value_objects.value_object import ValueObject
{% else %}
from {{ general.source_name }}.errors.incorrect_value_type_error import IncorrectValueTypeError
from {{ general.source_name }}.errors.invalid_id_format_error import InvalidIdFormatError
from {{ general.source_name }}.errors.required_value_error import RequiredValueError
from {{ general.source_name }}.value_objects.decorators.validation import validate
from {{ general.source_name }}.value_objects.value_object import ValueObject
{% endif %}


class Uuid(ValueObject[str]):
    @validate
    def _ensure_has_value(self, value: str) -> None:
        if value is None:
            raise RequiredValueError

    @validate
    def _ensure_value_is_string(self, value: str) -> None:
        if not isinstance(value, str):
            raise IncorrectValueTypeError(value)

    @validate
    def _ensure_value_has_valid_uuid_format(self, value: str) -> None:
        try:
            UUID(value)
        except ValueError:
            raise InvalidIdFormatError