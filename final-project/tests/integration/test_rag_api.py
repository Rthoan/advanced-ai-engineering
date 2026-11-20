from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_rag_api_returns_grounded_answer_with_citation():
    response = client.post(
        "/v1/chat",
        json={
            "message": "What is the return window?"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["route"] == "rag"
    assert "30 days" in data["answer"]

    assert len(data["citations"]) > 0
    assert data["citations"][0]["document_id"] == "return_policy"


def test_rag_api_abstains_when_evidence_is_missing():
    response = client.post(
        "/v1/chat",
        json={
            "message": "What is the CEO favorite movie policy?"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["route"] == "rag"
    assert "could not find enough trusted information" in data["answer"]
    assert data["citations"] == []
