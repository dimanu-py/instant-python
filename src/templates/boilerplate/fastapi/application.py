from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from {{ source_name }}.delivery.api.lifespan import lifespan
from {{ source_name}}.shared.infra.http.http_response import HttpResponse
from {{ source_name}}.shared.infra.http.status_code import StatusCode
from {{ source_name }}.shared.domain.exceptions.domain_error import DomainError

app = FastAPI(lifespan=lifespan)


@app.exception_handler(Exception)
async def unexpected_exception_handler(_: Request, exc: Exception) -> JSONResponse:
	return HttpResponse.internal_error(exc)


@app.exception_handler(DomainError)
async def domain_error_handler(_: Request, exc: DomainError) -> JSONResponse:
	return HttpResponse.domain_error(exc, status_code=StatusCode.BAD_REQUEST)
