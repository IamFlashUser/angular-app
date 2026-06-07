from rest_framework import serializers

from media.models import City

class CitySerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField(source="country.id", read_only=True)
    country_name = serializers.CharField(source="country.name", read_only=True)

    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "wikipedia_link",
            "country_id",
            "country_name",
            "capital",
        ]
