from typing import Any

from pydantic import BaseModel


class ErrorDetails(BaseModel):
    code: str
    message: str
    retryable: bool
    request_id: str | None = None


class ErrorResponse(BaseModel):
    error: ErrorDetails


class HealthResponse(BaseModel):
    status: str
    service: str


class ChatRequest(BaseModel):
    message: str


class Citation(BaseModel):
    document_id: str
    section: str | None = None


class ChatResponse(BaseModel):
    request_id: str
    answer: str
    route: str
    citations: list[Citation] = []


class ToolResult(BaseModel):
    status: str
    data: dict[str, Any] | None = None
    error: ErrorDetails | None = None