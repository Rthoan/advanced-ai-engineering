from app.rag.loader import load_markdown_documents


def test_load_policy_documents():
    chunks = load_markdown_documents("data/policies")

    assert len(chunks) > 0

    document_ids = {chunk.document_id for chunk in chunks}

    assert "return_policy" in document_ids
    assert "shipping_policy" in document_ids
    assert "product_faq" in document_ids


def test_return_policy_contains_return_window():
    chunks = load_markdown_documents("data/policies")

    matching = [
        chunk
        for chunk in chunks
        if chunk.document_id == "return_policy"
        and chunk.section == "Return Window"
    ]

    assert len(matching) == 1
    assert "30 days" in matching[0].content
