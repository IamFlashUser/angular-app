# backend-django

API REST Django pour l'application `media`.

## Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- pytest

## Base PostgreSQL

Le schéma PostgreSQL existe déjà.

Django ne crée pas les tables.

Configuration utilisée :

```text
database: media
user: postgres
password: Trustno1
host: localhost
port: 5432
```

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Vérification Django

```bash
python manage.py check
```

## Lancement

```bash
python manage.py runserver
```

## API

```text
GET /api/health

GET /api/continents
GET /api/continents/{id}

GET /api/countries
GET /api/countries/{id}

GET /api/cities
GET /api/cities/{id}

GET /api/persons
GET /api/persons/{id}

GET /api/professions
GET /api/professions/{id}

GET /api/media-types
GET /api/media-types/{id}

GET /api/media
GET /api/media/{id}
```

## Tests

```bash
pytest
```

## Important

Ne pas exécuter :

```bash
python manage.py makemigrations
python manage.py migrate
```

Les tables sont gérées directement dans PostgreSQL.
