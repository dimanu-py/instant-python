from fastapi import FastAPI
{% if "logger" in template.built_in_features %}
from fastapi.errors import RequestValidationError
{% endif %}

{% if template.name == template_types.STANDARD %}
{% if "logger" in template.built_in_features %}
from {{ general.source_name }}.api.handlers.error_handlers import (
	unexpected_exception_handler,
	domain_error_handler,
	validation_error_handler,
)
{% else %}
from {{ general.source_name }}.api.handlers.error_handlers import (
	unexpected_exception_handler,
	domain_error_handler,
)
{% endif %}
{% else %}
{% if "logger" in template.built_in_features %}
from {{ general.source_name }}.delivery.api.handlers.error_handlers import (
	unexpected_exception_handler,
	domain_error_handler,
	validation_error_handler,
)
{% else %}
from {{ general.source_name }}.delivery.api.handlers.error_handlers import (
	unexpected_exception_handler,
	domain_error_handler,
)
{% endif %}
{% endif %}

{% if ["async_alembic"] | is_in(template.built_in_features) %}
{% if template.name == template_types.STANDARD %}
from {{ general.source_name }}.api.lifespan import lifespan
{% else %}
from {{ general.source_name }}.delivery.api.lifespan import lifespan
{% endif %}
{% endif %}
from {{ general.source_name }}{{ "shared.domain.errors.domain_error" | resolve_import_path(template.name) }} import DomainError
{% if "logger" in template.built_in_features %}
from {{ general.source_name }}{{ "shared.infra.logger.file_logger" | resolve_import_path(template.name) }} import create_file_logger
{% if template.name == template_types.STANDARD %}
from {{ general.source_name }}.api.middleare.fast_api_log_middleware import FastapiLogMiddleware
{% else %}
from {{ general.source_name }}.delivery.api.middleare.fast_api_log_middleware import FastapiLogMiddleware
{% endif %}
{% endif %}


{% if ["async_alembic"] | is_in(template.built_in_features) %}
app = FastAPI(lifespan=lifespan)
{% else %}
app = FastAPI()
{% endif %}

{% if "logger" in template.built_in_features %}
logger = create_file_logger(name="{{ general.slug }}")

app.add_middleware(FastapiLogMiddleware, logger=logger)
app.add_exception_handler(RequestValidationError, validation_error_handler)
{% endif %}
app.add_exception_handler(Exception, unexpected_exception_handler)
app.add_exception_handler(DomainError, domain_error_handler)
