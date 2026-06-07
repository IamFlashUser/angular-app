from rest_framework import serializers

from media.models import Continent

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = [
            "id",
            "code",
            "name",
            "wikipedia_link",
            "area",
            "population",
            "countries_number",
        ]
