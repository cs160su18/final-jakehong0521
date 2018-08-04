from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.serializers import serialize
from las.models import *
import json

def index(request):
  return render(request, 'las/index.html')