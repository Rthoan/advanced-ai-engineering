from fastapi import APIRouter, Request

from app.core.errors import AppError
from app.models.schemas import ChatRequest, ChatResponse
from app.rag.service import RAGService
from app.services.router import Route, detect_route


router = APIRouter(prefix="/v1")

rag_service = RAGService()


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest, request: Request):
    message = payload.message.strip()

    if len(message) < 3:
        raise AppError(
            code="INVALID_REQUEST",
            message="Message must contain at least 3 characters.",
            status_code=422,
            retryable=False,
        )

    route = detect_route(message)

    if route == Route.RAG:
        result = rag_service.answer(
            query=message,
            top_k=3,
        )

        return ChatResponse(
            request_id=request.state.request_id,
            answer=result.answer,
            route=route.value,
            citations=result.citations,
        )

    return ChatResponse(
        request_id=request.state.request_id,
        answer="Route detected successfully.",
        route=route.value,
        citations=[],
    )
