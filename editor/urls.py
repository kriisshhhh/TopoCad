from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('generate_cube/', views.generate_cube, name='generate_cube'),
]

