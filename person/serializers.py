from rest_framework import serializers
from person.models import Person

class PersonSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Person
        fields = ['id','name', 'last_name', 'photo', 'cardnum', 'city', 'sex', 'personalid', 'department', 'characteristics', 'dateofbirth', 'dateofexpiry']

    def get_department(self,obj):
        return obj.ChilrdDepartment1