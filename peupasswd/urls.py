from django.contrib import admin
from django.urls import path, include, re_path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('peupasswd', views.peupasswd),
    re_path(r'.*', include('home.urls')),
]
