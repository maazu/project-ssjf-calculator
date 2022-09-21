
from django.urls import path
from .import views


from calculator import views

urlpatterns = [
    path('add/',  views.add, name='add'),
    path('subtract/',  views.subtract, name='subtract'),
]
