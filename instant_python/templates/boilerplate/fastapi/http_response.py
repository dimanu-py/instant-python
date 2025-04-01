{% set template_domain_import = "shared.domain"|compute_base_path(template) %}
{% set template_infra_import = "shared.infra"|compute_base_path(template) %}
from fastapi.responses import JSONResponse

from {{ source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError
from {{ source_name }}.{{ template_infra_import }}.http.status_code import StatusCode
from {{ source_name }}.{{ template_infra_import }}.log.logger import create_logger

logger = create_logger("logger")


class HttpResponse:
	@staticmethod
	def domain_error(error: DomainError, status_code: StatusCode) -> JSONResponse:
		logger.error(
			"error - domain error",
			extra={"extra": {"error": error.to_dict(), "status_code": status_code}},
		)
		return JSONResponse(content={"error": error.to_dict()}, status_code=status_code)

	@staticmethod
	def internal_error(error: Exception) -> JSONResponse:
		logger.error(
			"error - internal server error",
			extra={
				"extra": {"error": str(error)},
				"status_code": StatusCode.INTERNAL_SERVER_ERROR,
			},
		)
		return JSONResponse(
			content={"error": "Internal server error"},
			status_code=StatusCode.INTERNAL_SERVER_ERROR,
		)

	@staticmethod
	def created(resource: str) -> JSONResponse:
		logger.info(
			f"resource - {resource}",
			extra={"extra": {"status_code": StatusCode.CREATED}},
		)
		return JSONResponse(content={}, status_code=StatusCode.CREATED)

	@staticmethod
	def ok(content: dict) -> JSONResponse:
		return JSONResponse(content=content, status_code=StatusCode.OK)