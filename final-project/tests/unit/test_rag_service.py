from app.rag.service import RAGService


def test_rag_service_returns_context_and_citations():
    service = RAGService()

    result = service.answer(
        "What is the return window?",
        top_k=1,
    )

    assert "30 days" in result.answer
    assert len(result.citations) == 1
    assert result.citations[0].document_id == "return_policy"
    assert result.citations[0].section == "Return Window"


def test_rag_service_abstains_without_context():
    service = RAGService()

    result = service.answer(
        "What is the CEO's favorite movie?",
        top_k=3,
    )

    assert "could not find enough trusted information" in result.answer
    assert result.citations == []
