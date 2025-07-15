from fastapi.responses import JSONResponse


{% if ["logger"] | is_in(template.built_in_features) %}
logger = create_logger("logger")


class HttpResponse:
	@staticmethod
	def domain_error(error: DomainError, status_code: StatusCode) -> JSONResponse:
		logger.error(
			"error - domain error",
			extra={"extra": {"error": error.to_primitives(), "status_code": status_code}},
		)
		return JSONResponse(content={"error": error.to_primitives()}, status_code=status_code)

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
{% else %}
class HttpResponse:
	@staticmethod
	def domain_error(error: DomainError, status_code: StatusCode) -> JSONResponse:
		return JSONResponse(content={"error": error.to_primitives()}, status_code=status_code)

	@staticmethod
	def internal_error(error: Exception) -> JSONResponse:
		return JSONResponse(
			content={"error": "Internal server error"},
			status_code=StatusCode.INTERNAL_SERVER_ERROR,
		)

	@staticmethod
	def created(resource: str) -> JSONResponse:
		return JSONResponse(content={"resource": resource}, status_code=StatusCode.CREATED)

	@staticmethod
	def ok(content: dict) -> JSONResponse:
		return JSONResponse(content=content, status_code=StatusCode.OK)
{% endif %}