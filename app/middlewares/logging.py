import logging
import uuid
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        logger.info(f"Request {request_id} started: {request.method} {request.url}")
        
        try:
            response = await call_next(request)
            logger.info(f"Request {request_id} completed: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Request {request_id} failed: {str(e)}")
            raise

def setup_logging_middleware(app: FastAPI):
    app.add_middleware(RequestLoggingMiddleware)
