"""Main test file"""
from fastapi.testclient import TestClient

from app.main import NEWS, app

client = TestClient(app)

#
def test_read_root():
    """Ensure 200 on index endpoint"""
    response = client.get("/")
    assert response.status_code == 200


def test_read_articles():
    """ Ensure 200 on news endpoint"""
    response = client.get("/news")
    assert response.status_code == 200
    assert response.json() == NEWS


def test_read_article_success():
    """Ensure 200 on existing article"""
    response = client.get("/news/1")
    assert response.status_code == 200
    assert response.json() == NEWS[0]


def test_read_article_fail():
    """Ensure 404 on non-existing article"""
    response = client.get("/news/3")
    assert response.status_code == 404
