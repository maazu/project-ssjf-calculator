from django.urls import path

from .views.calculator import add

urlpatterns = [
    path('add/',  add.as_view(), name='clients-list'),

]
