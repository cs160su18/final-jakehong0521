from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('category/', views.category, name='category'),
  path('posting/', views.posting, name='posting'),
  path('guide/', views.guide, name='guide'),
  path('login/', views.login, name='login'),
  path('search/', views.search, name='search'),
  path('myCollections/', views.myCollections, name='myCollections'),
  
  url(r'^register/$', views.UserFormView.as_view(), name='register')
]