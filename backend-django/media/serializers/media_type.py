from rest_framework import serializers

from media.models import MediaType

class MediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaType
        fields = [
            "id",
            "name",
            "slug",
        ]
