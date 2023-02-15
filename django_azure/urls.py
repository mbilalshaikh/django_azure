# django_azure_demo/urls.py
from django.conf.urls import  include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    #path('', include('demoapp.urls')),
    path('admin/', admin.site.urls),

    path('', include('demoapp.urls')),

]