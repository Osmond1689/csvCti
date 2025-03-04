from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={
                    "message": "Internal server error",
                    "detail": str(e)
                }
            )

def setup_error_handler_middleware(app: FastAPI):
    app.add_middleware(ErrorHandlerMiddleware) 