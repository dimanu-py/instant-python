from abc import ABC

from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


class ErrorResponse(ABC, BaseModel):
	status_code: int
	detail: str

	def as_json(self) -> JSONResponse:
		return JSONResponse(
			content={"detail": self.detail},
			status_code=self.status_code,
		)


class UnprocessableEntityError(ErrorResponse):
	status_code: int = Field(default=status.HTTP_422_UNPROCESSABLE_ENTITY)
	detail: str = Field(default="Unprocessable Entity")


class ResourceNotFoundError(ErrorResponse):
	status_code: int = Field(default=status.HTTP_404_NOT_FOUND)
	detail: str = Field(default="Not Found")


class InternalServerError(ErrorResponse):
	status_code: int = Field(default=status.HTTP_500_INTERNAL_SERVER_ERROR)
	detail: str = Field(default="An unexpected error occurred.")
