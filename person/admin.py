from django.contrib import admin
from person.models import Characteristics,ChildDepartment,ParentDepartment,Person,sex, Monitoring
# Register your models here.

admin.site.register(sex)
admin.site.register(Characteristics)
admin.site.register(Person)
admin.site.register(ParentDepartment)
admin.site.register(ChildDepartment)
admin.site.register(Monitoring)
