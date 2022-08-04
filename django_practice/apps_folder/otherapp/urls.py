from django.urls import path
from .views import say_hi


app_name = "otherapp"
urlpatterns = [
    path("hola/", view=say_hi, name="hola"),
    path("/", view=say_hi, name="hola"),
]
