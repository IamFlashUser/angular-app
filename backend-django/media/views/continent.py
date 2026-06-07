from rest_framework.decorators import api_view
from rest_framework.response import Response

from media.models import Continent
from media.serializers import ContinentSerializer

@api_view(["GET"])
def continents(request):
    queryset = Continent.objects.all().order_by("id")
    serializer = ContinentSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def continent_detail(request, pk):
    continent = Continent.objects.get(pk=pk)
    serializer = ContinentSerializer(continent)
    return Response(serializer.data)
