import pytest

@pytest.mark.django_db
def test_get_cities(client):
    response = client.get("/api/cities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 10
    assert data[0]["id"] >= 1000
    assert "name" in data[0]
    assert "country_id" in data[0]
    assert "country_name" in data[0]

@pytest.mark.django_db
def test_get_city_detail(client):
    response = client.get("/api/cities/1000")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1000
    assert "name" in data
    assert "country_name" in data
