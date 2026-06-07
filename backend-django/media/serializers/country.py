from rest_framework import serializers

from media.models import Country

class CountrySerializer(serializers.ModelSerializer):
    continent_id = serializers.IntegerField(source="continent.id", read_only=True)
    continent_name = serializers.CharField(source="continent.name", read_only=True)

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "wikipedia_link",
            "continent_id",
            "continent_name",
            "iso_numeric",
            "iso_alpha2",
            "iso_alpha3",
            "flag",
        ]
