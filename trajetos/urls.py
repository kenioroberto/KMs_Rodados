from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:trajeto_id>', views.ver_trajeto, name='ver_trajeto'),
]
