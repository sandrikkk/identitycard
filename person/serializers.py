from rest_framework import serializers
from person.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name', 'last_name', 'photo', 'cardnum', 'city', 'sex', 'personalid', 'department', 'characteristics', 'dateofbirth', 'dateofexpiry']
