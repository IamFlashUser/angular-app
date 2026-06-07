from rest_framework.decorators import api_view
from rest_framework.response import Response

from media.models import Country
from media.serializers import CountrySerializer

@api_view(["GET"])
def countries(request):
    queryset = Country.objects.select_related("continent").all().order_by("id")
    serializer = CountrySerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def country_detail(request, pk):
    country = Country.objects.select_related("continent").get(pk=pk)
    serializer = CountrySerializer(country)
    return Response(serializer.data)
