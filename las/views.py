from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
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
  posts = Post.objects.filter(poster=request.user)
  print(posts)
  return render(request, 'las/myCollections.html')

def post_making(request):
  print(request.POST)
  if request.method == "POST":
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
    print('#####################')
    print(request.POST['content'])
    print(request.user)
    print('post_making request received')
    post = Post(poster=request.user, content=request.POST['content'])
    post.save()
    print(post.pk)
    print('#####################')
    postid = post.pk
    return HttpResponse('../' + str(post.pk))
  else:
    return render(request, 'las/post_making.html')

def post(request, post_id):
  post = Post.objects.get(pk=post_id)
  poster = post.poster
  return render(request, 'las/post.html', {'post': post, 'poster': poster})
  
def guide(request):
  return render(request, 'las/guide.html')

def search(request):
  return render(request, 'las/search.html')

def signup(request):
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
          
  return render(request, 'las/index.html')

def signin(request):
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
  return render(request, 'las/signinup.html', {'userform': UserForm(None), 'profileform': ProfileForm(None)})

def logout_view(request):
  logout(request)
  return render(request, 'las/logout_view.html')