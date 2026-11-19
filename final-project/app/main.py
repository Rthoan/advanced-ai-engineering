import uuid

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.routes import router as api_router
from app.core.errors import AppError
from app.models.schemas import ErrorDetails, ErrorResponse, HealthResponse


app = FastAPI(
    title="Production AI Customer Support Assistant",
    version="0.1.0",
)

app.include_router(api_router)


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())

    request.state.request_id = request_id

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id

    return response


@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    request_id = getattr(request.state, "request_id", None)

    response = ErrorResponse(
        error=ErrorDetails(
            code=exc.code,
            message=exc.message,
            retryable=exc.retryable,
            request_id=request_id,
        )
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(),
    )


@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(
        status="ok",
        service="production-ai-customer-support",
    )
