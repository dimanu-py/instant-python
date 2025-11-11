from {{ general.source_name }}{{ "shared.domain.errors.base_error" | resolve_import_path(template.name) }} import BaseError


class DomainError(BaseError):
    ...

