from .models import Person
from person.serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
class PersonsIdentity(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many = True)
        return Response(serializer.data)
