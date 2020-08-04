from fastapi.testclient import TestClient
from app import app, NEWS

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_articles():
    response = client.get("/news")
    assert response.status_code == 200
    assert response.json() == NEWS

def test_read_article_success():
    response = client.get("/news/1")
    assert response.status_code == 200
    assert response.json() == NEWS[0]

def test_read_article_fail():
    response = client.get("/news/3")
    assert response.status_code == 404

