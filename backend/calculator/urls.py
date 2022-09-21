from django.urls import path

from .views.calculator import add

urlpatterns = [
    path('add/',  add.as_view(), name='add'),
    path('subtract/',  add.as_view(), name='subtract'),
]
