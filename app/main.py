from fastapi import FastAPI
from app.middlewares.cors import setup_cors_middleware
from app.middlewares.timing import setup_timing_middleware
from app.middlewares.logging import setup_logging_middleware
from app.middlewares.error_handler import setup_error_handler_middleware
from app.api.v1.routers import user_router, csv_router, auth_router
from app.core.settings import Settings

app = FastAPI(
    title="CSV-CTI API",
    description="CSV Intelligence Analysis API",
    version="1.0.0"
)

# 注册中间件
setup_cors_middleware(app)
setup_timing_middleware(app)
setup_logging_middleware(app)
setup_error_handler_middleware(app)

# 注册路由
app.include_router(auth_router.router, prefix="/api/v1", tags=["auth"])
app.include_router(user_router.router, prefix="/api/v1/users", tags=["users"])
app.include_router(csv_router.router, prefix="/api/v1/csv", tags=["csv"])


@app.get("/")
async def root():
    return {"message": "Welcome to CSV-CTI API"}
