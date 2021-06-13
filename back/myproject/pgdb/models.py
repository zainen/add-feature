from django.db import models
# from view_table.models import ViewTable

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name

class Feature(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Like(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


# class Features(ViewTable):
