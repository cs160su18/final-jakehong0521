from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Post(models.Model):
  date = models.DateField(default=datetime.date.today())
  poster = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  
  def __str__(self):
    return self.poster.username + ' on ' + self.date.__str__()

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=40)
  aboutMe = models.TextField(blank=True)
  jobDescription = models.TextField(blank=True)
  star = models.IntegerField(default=0)
  company = models.CharField(max_length=40, blank=True)
  field = models.TextField(choices=(
    ('N/A', 'N/A'),
    ('administration', 'Administration'),
    ('banking', 'Banking'),
    ('design', 'Design'),
    ('education', 'Education'),
    ('engineering', 'Engineering'),
    ('entrepreneur', 'Entrepreneur'),
    ('government', 'Government'),
    ('health', 'Health'),
    ('legal', 'Legal'),
    ('media', 'Media'),
    ('research', 'Research'),
    ('sales', 'Sales')
  ), default='N/A')
  
  def __str__(self):
    return self.user.username + ' is ' + self.title