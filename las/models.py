from django.db import models
import datetime

need = 'need'
have = 'have'
history = 'history'

stateChoices = ((need, 'need'), (have, 'have'), (history, 'history'))

class User(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=10)
  
class Item(models.Model):
  name = models.CharField(max_length=50, blank=False)
  date = models.DateField(default=datetime.date.today())
  description = models.CharField(max_length=200, null=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  amount = models.IntegerField(default='1')
  state = models.CharField(max_length=10, choices = stateChoices, default=need)