from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from las.models import *
import json

# Create your views here.
def index(request):
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
  form_class = UserForm
  template_name = 'las/registration_form.html'
  
  def get(self, request):
    form = self.form_class(None)
    return render(request, self.template_name, {'form': form})
  
  def post(self, request):
    form = self.form_class(request.POST)
    
    if form.is_valid():
      user = form.save(commit=False)
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user.set_password(password)
      user.save()
      
      user = authenticate(username=username, password=password)
      
      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect('las:index')
        
    return render(request, self.template_name, {'form': form})