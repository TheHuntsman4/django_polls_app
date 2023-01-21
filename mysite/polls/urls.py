from django.urls import path

from . import views

urlpatterns = [
    path('ac', views.index, name='index'),
]