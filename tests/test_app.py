from fastapi.testclient import TestClient
from eksi_api.app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"name": "eksi-api", "version": "0.0.1-pretest"}


def test_search_topic():
    response = client.get("/topic/search/python")
    assert response.status_code == 200
    assert response.json()["title"] is not None
    assert response.json()["url"] is not None
    assert response.json()["page"] == 1
    assert response.json()["page_count"] is not None


def test_search_topic_with_entries():
    response = client.get("/entries/search/python")
    assert response.status_code == 200
    assert response.json()["title"] is not None
    assert response.json()["url"] is not None
    assert response.json()["page"] == 1
    assert response.json()["page_count"] is not None
    assert response.json()["entries"] is not None


def test_get_trending_topics():
    response = client.get("/topic/trending")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_trending_topic_details():
    response = client.get("/topic/trending/details")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for topic in response.json():
        assert topic["details"] is not None


def test_get_trending_entries():
    response = client.get("/entry/trending")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for topic in response.json():
        assert topic["entries"] is not None
