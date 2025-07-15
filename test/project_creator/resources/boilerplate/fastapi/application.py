from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

{% if ["async_alembic"] | is_in(template.built_in_features) %}
from src.api.lifespan
{% endif %}

{% if ["async_alembic"] | is_in(template.built_in_features) %}
app = FastAPI(lifespan=lifespan)
{% else %}
app = FastAPI()
{% endif %}

@app.exception_handler(Exception)
async def unexpected_exception_handler(_: Request, exc: Exception) -> JSONResponse:
	return HttpResponse.internal_error(exc)


@app.exception_handler(DomainError)
async def domain_error_handler(_: Request, exc: DomainError) -> JSONResponse:
	return HttpResponse.domain_error(exc, status_code=StatusCode.BAD_REQUEST)
