import pytest

@pytest.mark.django_db
def test_get_continents(client):
    response = client.get("/api/continents")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2
    assert data[0]["id"] >= 1000
    assert "code" in data[0]
    assert "name" in data[0]

@pytest.mark.django_db
def test_get_continent_detail(client):
    response = client.get("/api/continents/1000")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1000
    assert "code" in data
    assert "name" in data
