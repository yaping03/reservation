from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Conference(models.Model):
    name = models.CharField(max_length=36)

class People(models.Model):
    user = models.CharField(max_length=16)
    pwd = models.CharField(max_length=32)
    name= models.CharField(max_length=16)

class Timer(models.Model):
    timer=models.TimeField()

class Date(models.Model):
    date=models.DateField()

class Date2Timer(models.Model):
    nid = models.AutoField(primary_key=True)
    timer = models.ForeignKey("Timer")
    date = models.ForeignKey("Date")
    people = models.ForeignKey("People")
    confe = models.ForeignKey("Conference")
    class Meta:
        unique_together = [
            ('timer', 'date','confe'),
        ]