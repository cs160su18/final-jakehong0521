from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import *
from las.models import *
import json

# Create your views here.
def index(request):
  print('index view with ' + request.user.__str__())
  return render(request, 'las/index.html')

def category(request):
  return render(request, 'las/category.html')

def myCollections(request):
  return render(request, 'las/myCollections.html')

def post_making(request):
  return render(request, 'las/posting.html')

def guide(request):
  return render(request, 'las/guide.html')

def search(request):
  return render(request, 'las/search.html')

def signup(request):
  print('####################')
  print('signup post request')
  userForm = UserForm(request.POST)
  profileForm = ProfileForm(request.POST)
  if (userForm.is_valid() and profileForm.is_valid()):
    user = userForm.save(commit=False)
    profile = profileForm.save(commit=False)
    username = userForm.cleaned_data['username']
    password = userForm.cleaned_data['password']
    user.set_password(password)
    user.save()
    profile.user = user
    profile.save()

    user = authenticate(username=username, password=password)

    if user is not None:
      if user.is_active:
        login(request, user)
        print('created and signed in')
        print(user)
        print('########################')
        print(profile)
          
  return render(request, 'las/index.html')

def signin(request):
  print('####################')
  print('signin request')
  username = request.POST['username']
  password = request.POST['password']

  user = authenticate(username=username, password=password)

  if user is not None:
    if user.is_active:
      login(request, user)

  return redirect('../')

def signinup(request):
  userForm = UserForm
  profileForm = ProfileForm
  print('####################')
  print('signin get request')
  return render(request, 'las/signinup.html', {'userform': UserForm(None), 'profileform': ProfileForm(None)})

def logout_view(request):
  print('logout view')
  logout(request)
  return render(request, 'las/logout_view.html')