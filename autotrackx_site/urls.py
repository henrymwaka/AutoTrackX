from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpResponse

def health(_): return JsonResponse({"status":"ok","app":"AutoTrackX"})
def home(_): return HttpResponse("AutoTrackX is running")

urlpatterns = [
    path("", home, name="home"),
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
]
