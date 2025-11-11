from fastapi import Request
from fastapi.responses import JSONResponse
{% if "logger" in template.built_in_features %}
from fastapi.errors import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from {{ general.source_name }}{{ "shared.infra.logger.file_logger" | resolve_import_path(template.name) }} import create_file_logger
{% endif %}
from {{ general.source_name }}{{ "shared.infra.http.error_response" | resolve_import_path(template.name) }} import InternalServerError, UnprocessableEntityError
from {{ general.source_name }}{{ "shared.domain.errors.domain_error" | resolve_import_path(template.name) }} import DomainError


{% if "logger" in template.built_in_features %}
logger = create_file_logger(name="{{ general.slug }}")

async def unexpected_exception_handler(request: Request, exc: Exception) -> JSONResponse:
	logger.error(
		message=f"error - {request.url.path}",
		details={
			"error": {
				"message": str(exc),
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
			"error": {"message": exc.message},
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
			"error": {"message": str(exc)},
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