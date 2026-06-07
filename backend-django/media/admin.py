from django.contrib import admin

from .models import City, Continent, Country, Media, MediaType, Person, Profession

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Profession)
admin.site.register(MediaType)
admin.site.register(Media)
