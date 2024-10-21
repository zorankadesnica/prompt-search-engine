from fastapi.testclient import TestClient
from search_engine.api import app

client = TestClient(app)
def test_search_similar_prompts():
    response = client.post(
        "/search/",
        json={
            "query": "Explain deep learning.",
            "n": 3
        }
    )
    assert response.status_code == 200
    print( response.status_code)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3
    for item in data:
        assert "similarity_score" in item
        assert "prompt" in item
        assert isinstance(item["similarity_score"], float)
        assert isinstance(item["prompt"], str)

def test_search_missing_query():
    response = client.post(
        "/search/",
        json={
            "n": 3
        }
    )
    assert response.status_code == 422  # Unprocessable Entity

def test_search_invalid_n():
    response = client.post(
        "/search/",
        json={
            "query": "Explain deep learning.",
            "n": -5
        }
    )
    # Depending on your validation, adjust the expected status code
    # Here assuming n must be positive
    assert response.status_code == 500
