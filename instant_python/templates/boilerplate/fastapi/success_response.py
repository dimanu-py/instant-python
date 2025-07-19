from pydantic import BaseModel
from fastapi.responses import JSONResponse


class SuccessResponse(BaseModel):
	status_code: int
	data: dict

	def as_json(self) -> JSONResponse:
		return JSONResponse(
			content=self.data,
			status_code=self.status_code,
		)
