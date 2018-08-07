from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('category/', views.category, name='category'),
  path('post_making/', views.post_making, name='post_making'),
  path('guide/', views.guide, name='guide'),
  path('signinup/', views.signinup, name='signinup'),
  path('signin/', views.signin, name='signin'),
  path('signup/', views.signup, name='signup'),
  path('search/', views.search, name='search'),
  path('myCollections/', views.myCollections, name='myCollections'),
#   path('register/', views.UserFormView.as_view(), name='register'),
  path('logout_view/', views.logout_view, name='logout_view')
]