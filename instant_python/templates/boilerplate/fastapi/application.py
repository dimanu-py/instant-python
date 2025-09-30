{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
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
{% if template_domain_import %}
from {{ general.source_name }}.{{ template_domain_import }}.errors.domain_error import DomainError
{% else %}
from {{ general.source_name }}.errors.domain_error import DomainError
{% endif %}
{% if "logger" in template.built_in_features %}
{% if template_infra_import %}
from {{ general.source_name }}.{{ template_infra_import }}.logger.file_logger import create_file_logger
{% else %}
from {{ general.source_name }}.logger.file_logger import create_file_logger
{% endif %}
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
