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
  print(request.user)
  return render(request, 'las/index.html')

def category(request):
  return render(request, 'las/category.html')

def myCollections(request):
  return render(request, 'las/myCollections.html')

def posting(request):
  return render(request, 'las/posting.html')

def guide(request):
  return render(request, 'las/guide.html')

def search(request):
  return render(request, 'las/search.html')

def login(request):
  return render(request, 'las/login.html')

# testing

class UserFormView(View):
#   form_class = UserForm
  user_form = UserForm
  profile_form = ProfileForm
  template_name = 'las/registration_form.html'
  
  def get(self, request):
#     form = self.form_class(None)
#     return render(request, self.template_name, {'form': form})
    userForm = self.user_form(None)
    profileForm = self.profile_form(None)
    return render(request, self.template_name, {'userform': userForm, 'profileform': profileForm})
  
  def post(self, request):
    print(request.POST)
    userForm = self.user_form(request.POST)
    profileForm = self.profile_form(request.POST)
    if (userForm.is_valid() and profileForm.is_valid()):
      user = userForm.save(commit=False)
      username = userForm.cleaned_data['username']
      password = userForm.cleaned_data['password']
      user.set_password(password)
      print(user)
#       user.save()
    
    return render(request, 'las/index.html')
#     form = self.form_class(request.POST)
    
    
#     if form.is_valid():
#       user = form.save(commit=False)
#       username = form.cleaned_data['username']
#       password = form.cleaned_data['password']
#       user.set_password(password)
#       user.save()
      
#       user = authenticate(username=username, password=password)
      
#       if user is not None:
#         if user.is_active:
#           login(request, user)
#           return redirect('las:index')
        
#     return render(request, self.template_name, {'form': form})