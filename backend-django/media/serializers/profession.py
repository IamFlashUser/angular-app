from rest_framework import serializers

from media.models import Profession

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = [
            "id",
            "name",
            "slug",
        ]
