from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('slip/<prog>-<sem>-<rollNo>', views.slip, name="Slip"),
]
