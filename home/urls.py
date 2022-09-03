from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Peupasswd"),
    path('peupasswd', views.peupasswd, name="Peupasswd"),
]