{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_infra_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.base_error import BaseError
{% else %}
from {{ general.source_name }}.errors.base_error import BaseError
{% endif %}


class DomainError(Error):
    ...

