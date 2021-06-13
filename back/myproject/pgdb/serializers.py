from re import search
from django.db.models.fields import IntegerField
from rest_framework import serializers

class FeatureSerializer(serializers.Serializer):
  id = serializers.IntegerField(label='ID', read_only=True)
  name = serializers.CharField(max_length=200)

class UserSerializer(serializers.Serializer):
  id = serializers.IntegerField(label='ID', read_only=True)
  name = serializers.CharField(max_length=40)

class LikeSerializer(serializers.Serializer):
  id = serializers.IntegerField(label='ID', read_only=True)
  user_id = serializers.PrimaryKeyRelatedField(querySet=User.objects.all())
  feature_id = serializers.PrimaryKeyRelatedField(querySet=Feature.object.all())