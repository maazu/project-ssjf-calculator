
from django.urls import path
from .import views


from calculator import views

urlpatterns = [
    path('compute/',  views.calulator_funtions, name='caluator_function'),

]
