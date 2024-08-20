from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello/', views.say_hello) # Parameter 1 - path, Parameter 2 a view function that returns a HttpResponse end routes with /
]