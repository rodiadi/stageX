app_name = "core"

from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="dashboard"),
]