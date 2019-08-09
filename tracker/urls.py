from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracker, name='tracker'),
    path('add', views.add, name='add'),
]
