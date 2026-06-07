from django.urls import path

from .views import (
    cities,
    city_detail,
    continents,
    continent_detail,
    countries,
    country_detail,
    health,
    media,
    media_detail,
    media_types,
    media_type_detail,
    persons,
    person_detail,
    professions,
    profession_detail,
)

urlpatterns = [
    path("health", health),
    path("continents", continents),
    path("continents/<int:pk>", continent_detail),
    path("countries", countries),
    path("countries/<int:pk>", country_detail),
    path("cities", cities),
    path("cities/<int:pk>", city_detail),
    path("persons", persons),
    path("persons/<int:pk>", person_detail),
    path("professions", professions),
    path("professions/<int:pk>", profession_detail),
    path("media-types", media_types),
    path("media-types/<int:pk>", media_type_detail),
    path("media", media),
    path("media/<int:pk>", media_detail),
]
