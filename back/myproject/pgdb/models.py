from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=40)

class Feature(models.Model):
  name = models.CharField(max_length=200)

class Likes(models.Model):
  user_id = models.PositiveIntegerField()
  feature_id = models.PositiveIntegerField()
