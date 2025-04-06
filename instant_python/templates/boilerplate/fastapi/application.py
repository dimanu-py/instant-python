{% set template_domain_import = "shared.domain"|compute_base_path(template) %}
{% set template_infra_import = "shared.infra"|compute_base_path(template) %}
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

{% if template == template_types.STANDARD %}
from {{ source_name }}.api.lifespan import lifespan
{% else %}
from {{ source_name }}.delivery.api.lifespan import lifespan
{% endif %}
from {{ source_name }}.{{ template_infra_import }}.http.http_response import HttpResponse
from {{ source_name }}.{{ template_infra_import }}.http.status_code import StatusCode
from {{ source_name }}.{{ template_domain_import }}.exceptions.domain_error import DomainError

app = FastAPI(lifespan=lifespan)


@app.exception_handler(Exception)
async def unexpected_exception_handler(_: Request, exc: Exception) -> JSONResponse:
	return HttpResponse.internal_error(exc)


@app.exception_handler(DomainError)
async def domain_error_handler(_: Request, exc: DomainError) -> JSONResponse:
	return HttpResponse.domain_error(exc, status_code=StatusCode.BAD_REQUEST)
