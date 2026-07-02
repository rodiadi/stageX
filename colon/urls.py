from django.urls import path

from . import views



app_name = "colon"



urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),


    path(
        "staging/",
        views.staging,
        name="staging"
    ),

]