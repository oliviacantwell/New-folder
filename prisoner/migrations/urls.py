from django.urls import path
from prisoner import views

urlpatterns = [
    path("prisoner/", views.prisoner, name="prisoner"),
]