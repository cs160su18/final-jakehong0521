from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from las.models import *
from django.contrib.auth import (
authenticate, get_user_model, login, logout)
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