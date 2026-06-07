from rest_framework import serializers

from media.models import Media

class MediaSerializer(serializers.ModelSerializer):
    type_id = serializers.IntegerField(source="type.id", read_only=True)
    type_name = serializers.CharField(source="type.name", read_only=True)
    persons = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Media
        fields = [
            "id",
            "title",
            "slug",
            "type_id",
            "type_name",
            "release_year",
            "description",
            "persons",
        ]
