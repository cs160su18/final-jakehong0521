from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('category/', views.category, name='category'),
  path('posting/', views.posting, name='posting'),
  path('myCollections/', views.myCollections, name='myCollections')
]