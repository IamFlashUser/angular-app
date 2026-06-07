import pytest

@pytest.mark.django_db
def test_get_media(client):
    response = client.get("/api/media")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 10
    assert data[0]["id"] >= 1000
    assert "title" in data[0]
    assert "slug" in data[0]
    assert "type_id" in data[0]
    assert "type_name" in data[0]
    assert "release_year" in data[0]
    assert "description" in data[0]
    assert "persons" in data[0]

@pytest.mark.django_db
def test_get_media_detail(client):
    response = client.get("/api/media/1004")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1004
    assert data["title"] == "Inception"
    assert data["slug"] == "inception"
    assert data["type_name"] == "Movie"
    assert data["release_year"] == 2010
    assert "Christopher Nolan" in data["persons"]
