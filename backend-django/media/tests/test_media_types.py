import pytest

@pytest.mark.django_db
def test_get_media_types(client):
    response = client.get("/api/media-types")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["id"] >= 1000
    assert "name" in data[0]
    assert "slug" in data[0]

@pytest.mark.django_db
def test_get_media_type_detail(client):
    response = client.get("/api/media-types/1000")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1000
    assert data["slug"] == "movie"
