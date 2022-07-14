from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ambiente_id>', views.ver_ambiente, name='ver_ambiente'),
    
]
