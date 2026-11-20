from app.rag.loader import load_markdown_documents
from app.rag.retriever import retrieve_chunks


def test_retrieve_return_window():
    chunks = load_markdown_documents("data/policies")

    results = retrieve_chunks(
        "What is the return window?",
        chunks,
        top_k=2,
    )

    assert len(results) > 0
    assert results[0].chunk.document_id == "return_policy"
    assert results[0].chunk.section == "Return Window"
    assert results[0].score > 0


def test_retrieve_shipping_policy():
    chunks = load_markdown_documents("data/policies")

    results = retrieve_chunks(
        "How long does standard shipping take?",
        chunks,
        top_k=2,
    )

    assert len(results) > 0
    assert results[0].chunk.document_id == "shipping_policy"
    assert results[0].chunk.section == "Standard Shipping"
    assert results[0].score > 0
