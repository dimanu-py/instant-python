{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% set template_infra_import = "shared.infra"|compute_base_path(template.name) %}
from fastapi import Request
from fastapi.responses import JSONResponse
{% if "logger" in template.built_in_features %}
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from {{ general.source_name }}.{{ template_infra_import }}.logger.file_logger import create_file_logger
{% endif %}
from {{ general.source_name }}.{{ template_infra_import }}.http.error_response import InternalServerError, UnprocessableEntityError
from {{ general.source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError


{% if "logger" in template.built_in_features %}
logger = create_file_logger(name="{{ general.slug }}")

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


async def validation_error_handler(
		request: Request,
		exc: RequestValidationError,
) -> JSONResponse:
	logger.error(
		message=f"error - {request.url.path}",
		details={
			"error": {"message": str(exc), "type": "validation_error"},
			"method": request.method,
			"source": request.url.path,
		},
	)
	return await request_validation_exception_handler(request, exc)
{% else %}
async def unexpected_exception_handler(_: Request, __: Exception) -> JSONResponse:
	return InternalServerError().as_json()


async def domain_error_handler(_: Request, __: DomainError) -> JSONResponse:
	return UnprocessableEntityError().as_json()
{% endif %}