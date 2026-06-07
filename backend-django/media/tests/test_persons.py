import pytest

@pytest.mark.django_db
def test_get_persons(client):
    response = client.get("/api/persons")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 10
    assert data[0]["id"] >= 1000
    assert "name" in data[0]
    assert "wikipedia_link" in data[0]
    assert "birth_date" in data[0]
    assert "birth_city_name" in data[0]
    assert "birth_country_name" in data[0]
    assert "nationalities" in data[0]
    assert "professions" in data[0]

@pytest.mark.django_db
def test_get_person_detail(client):
    response = client.get("/api/persons/1004")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1004
    assert data["name"] == "Christopher Nolan"
    assert data["wikipedia_link"] == "Christopher_Nolan"
    assert data["birth_city_name"] == "London"
    assert data["birth_country_name"] == "United Kingdom"
    assert "United Kingdom" in data["nationalities"]
    assert "Director" in data["professions"]
