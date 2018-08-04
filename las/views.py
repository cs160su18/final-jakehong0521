from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from las.models import *
import json

# Create your views here.
def index(request):
  return render(request, 'las/index.html')