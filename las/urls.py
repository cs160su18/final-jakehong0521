from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('category/', views.category, name='category'),
  path('posting/', views.posting, name='posting'),
  path('guide/', views.guide, name='guide'),
  path('signin/', views.signin, name='signin'),
  path('search/', views.search, name='search'),
  path('myCollections/', views.myCollections, name='myCollections'),
  
  path('register/', views.UserFormView.as_view(), name='register'),
  path('logout_view/', views.logout_view, name='logout_view')
]