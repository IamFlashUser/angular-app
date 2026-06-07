import pytest

@pytest.mark.django_db
def test_get_countries(client):
    response = client.get("/api/countries")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3
    assert data[0]["id"] >= 1000
    assert "name" in data[0]
    assert "continent_id" in data[0]
    assert "continent_name" in data[0]
    assert "iso_alpha2" in data[0]

@pytest.mark.django_db
def test_get_country_detail(client):
    response = client.get("/api/countries/1000")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1000
    assert "name" in data
    assert "iso_alpha2" in data
