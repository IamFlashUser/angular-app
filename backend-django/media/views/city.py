from rest_framework.decorators import api_view
from rest_framework.response import Response

from media.models import City
from media.serializers import CitySerializer

@api_view(["GET"])
def cities(request):
    queryset = City.objects.select_related("country").all().order_by("id")
    serializer = CitySerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def city_detail(request, pk):
    city = City.objects.select_related("country").get(pk=pk)
    serializer = CitySerializer(city)
    return Response(serializer.data)
