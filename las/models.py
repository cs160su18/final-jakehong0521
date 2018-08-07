from django.db import models
from django.contrib.auth.models import User
import datetime

class Post(models.Model):
  date = models.DateField(default=datetime.date.today())
  poster = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  
  def __str__(self):
    return self.poster.username + ' on ' + self.date

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=40)
  aboutMe = models.TextField()
  star = models.IntegerField(default=0)
  company = models.CharField(max_length=40, blank=True)