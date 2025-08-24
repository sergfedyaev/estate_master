from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(_): 
    return HttpResponse("OK")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
]
