from django.urls import path
from person import views

urlpatterns = [
    path("", views.Persons.as_view())
]
