from app.services.router import Route, detect_route


def test_order_lookup_route():
    route = detect_route("Where is order ORD-100?")
    assert route == Route.ORDER_LOOKUP


def test_create_return_route():
    route = detect_route("I want to return ORD-100")
    assert route == Route.CREATE_RETURN


def test_rag_route():
    route = detect_route("What is your return policy?")
    assert route == Route.RAG


def test_fallback_route():
    route = detect_route("Tell me a joke")
    assert route == Route.FALLBACK