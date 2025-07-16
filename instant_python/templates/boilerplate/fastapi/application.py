{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

{% if ["async_alembic"] | is_in(template.built_in_features) %}
{% if template.name == template_types.STANDARD %}
from {{ general.source_name }}.api.lifespan import lifespan
{% else %}
from {{ general.source_name }}.delivery.api.lifespan import lifespan
{% endif %}
{% endif %}
from {{ general.source_name }}.{{ template_infra_import }}.http.error_response import InternalServerError, UnprocessableEntityError, ResourceNotFoundError
from {{ general.source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError
{% if "logger" in template.built_in_features %}
from {{ general.source_name }}.{{ template_infra_import }}.logger.fastapi_file_logger import create_api_logger
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

@app.exception_handler(Exception)
async def unexpected_exception_handler(request: Request, exc: Exception) -> JSONResponse:
	logger.error(
		message=f"error - {request.url.path}",
		details={
			"error": {
				"message": str(exc),
				"type": "unexpected_error",
			},
			"method": request.method,
			"source": request.url.path,
		},
	)
	return InternalServerError().as_json()


@app.exception_handler(DomainError)
async def domain_error_handler(request: Request, exc: DomainError) -> JSONResponse:
	logger.error(
		message=f"error - {request.url.path}",
		details={
			"error": exc.to_primitives(),
			"method": request.method,
			"source": request.url.path,
		},
	)
	return UnprocessableEntityError().as_json()
{% else %}
@app.exception_handler(Exception)
async def unexpected_exception_handler(_: Request, __: Exception) -> JSONResponse:
	return InternalServerError().as_json()


@app.exception_handler(DomainError)
async def domain_error_handler(_: Request, __: DomainError) -> JSONResponse:
	return UnprocessableEntityError().as_json()
{% endif %}

