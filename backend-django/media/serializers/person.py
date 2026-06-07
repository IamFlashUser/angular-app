from rest_framework import serializers

from media.models import Person

class PersonSerializer(serializers.ModelSerializer):
    birth_city_id = serializers.IntegerField(source="birth_city.id", read_only=True)
    birth_city_name = serializers.CharField(source="birth_city.name", read_only=True)
    birth_country_name = serializers.CharField(source="birth_city.country.name", read_only=True)
    nationalities = serializers.StringRelatedField(many=True, read_only=True)
    professions = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "wikipedia_link",
            "birth_date",
            "birth_city_id",
            "birth_city_name",
            "birth_country_name",
            "death_date",
            "gender_id",
            "image",
            "nationalities",
            "professions",
        ]
