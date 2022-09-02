from django.contrib import admin
from person.models import Characteristics,ChildDepartment,ParentDepartment,Person,sex, Monitoring
# Register your models here.


# admin.site.register(Monitoring)

class MonitoringInline(admin.StackedInline):
    model = Monitoring
    extra = 0
    fields = ['movida', 'wavida', 'comment']

class PersonAdmin(admin.ModelAdmin):
    inlines = [MonitoringInline]
    list_display = ['name', 'last_name']

admin.site.register(Person, PersonAdmin)




admin.site.register(sex)
admin.site.register(Characteristics)
admin.site.register(ParentDepartment)
admin.site.register(ChildDepartment)

