from rest_framework.decorators import api_view
from rest_framework.response import Response

from media.models import MediaType
from media.serializers import MediaTypeSerializer

@api_view(["GET"])
def media_types(request):
    queryset = MediaType.objects.all().order_by("id")
    serializer = MediaTypeSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def media_type_detail(request, pk):
    media_type = MediaType.objects.get(pk=pk)
    serializer = MediaTypeSerializer(media_type)
    return Response(serializer.data)
