from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu.index'),
    path('menu/', views.menu, name='menu.menu'),
]