from rest_framework.decorators import api_view
from rest_framework.response import Response

from media.models import Person
from media.serializers import PersonSerializer

@api_view(["GET"])
def persons(request):
    queryset = (
        Person.objects
        .select_related("birth_city", "birth_city__country")
        .prefetch_related("nationalities", "professions")
        .all()
        .order_by("id")
    )
    serializer = PersonSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def person_detail(request, pk):
    person = (
        Person.objects
        .select_related("birth_city", "birth_city__country")
        .prefetch_related("nationalities", "professions")
        .get(pk=pk)
    )
    serializer = PersonSerializer(person)
    return Response(serializer.data)
