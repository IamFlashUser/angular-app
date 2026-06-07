from rest_framework.decorators import api_view
from rest_framework.response import Response

from media.models import Media
from media.serializers import MediaSerializer

@api_view(["GET"])
def media(request):
    queryset = (
        Media.objects
        .select_related("type")
        .prefetch_related("persons")
        .all()
        .order_by("id")
    )
    serializer = MediaSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def media_detail(request, pk):
    item = (
        Media.objects
        .select_related("type")
        .prefetch_related("persons")
        .get(pk=pk)
    )
    serializer = MediaSerializer(item)
    return Response(serializer.data)
