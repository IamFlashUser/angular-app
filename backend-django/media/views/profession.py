from rest_framework.decorators import api_view
from rest_framework.response import Response

from media.models import Profession
from media.serializers import ProfessionSerializer

@api_view(["GET"])
def professions(request):
    queryset = Profession.objects.all().order_by("id")
    serializer = ProfessionSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def profession_detail(request, pk):
    profession = Profession.objects.get(pk=pk)
    serializer = ProfessionSerializer(profession)
    return Response(serializer.data)
