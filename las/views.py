from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from las.models import *
from django.contrib.auth import (
authenticate, get_user_model, login, logout)
from .forms import UserLoginForm
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

# testing user registration

def login_view(request):
  form = UserLoginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
  return render(request, 'form.html', {'form':form})

def logout_view(request):
  return render(request, 'form.html', {})

def register_view(request):
  return render(request, 'form.html', {})