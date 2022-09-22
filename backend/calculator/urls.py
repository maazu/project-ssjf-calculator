
from django.urls import path
from .import views


from calculator import views

urlpatterns = [
    path('add/',  views.add, name='add'),
    path('squareroot/',  views.square_root, name='squareroot'),
    path('subtract/',  views.subtract, name='subtract'),
    path('multiply/',  views.multiply, name='multiply'),
    path('divide/',  views.divide, name='divide'),
    path('factorial/',  views.factorial, name='factorial'),
    path('step4/',  views.step_four, name='step4'),
    path('squarerootcap/',  views.square_root_cap, name='squarerootcap'),
]
