from enum import StrEnum


class Route(StrEnum):
    RAG = "rag"
    ORDER_LOOKUP = "order_lookup"
    CREATE_RETURN = "create_return"
    FALLBACK = "fallback"


def detect_route(message: str) -> Route:
    text = message.lower()

    if "return" in text and "ord-" in text:
        return Route.CREATE_RETURN

    if "ord-" in text and any(
        word in text
        for word in ["where", "status", "track", "order"]
    ):
        return Route.ORDER_LOOKUP

    if any(
        word in text
        for word in ["policy", "shipping", "faq", "refund"]
    ):
        return Route.RAG

    return Route.FALLBACK