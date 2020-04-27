from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('next/', views.next, name='next'),
  path('cats/', views.cats_index, name='index')
]