from django.urls import path

from podomarket import views

urlpatterns = [
    path("", views.index, name="index"),
]