from .models import Monitoring, Person
from person.serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template 


class PersonsIdentity(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def generate_pdf(request):
    persons = Person.objects.all()
    monitoring = Monitoring.objects.all()
    template = get_template('pdf.html')
    html = template.render({'persons': persons, "monitorings": monitoring})
    pdf = pdfkit.from_string(html, False, options={})
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdf.pdf"'

    return response