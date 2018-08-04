from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.serializers import serialize
from life.models import User, Item
import json
from life.models import *

def index(request):
  return render(request, 'las/index.html')